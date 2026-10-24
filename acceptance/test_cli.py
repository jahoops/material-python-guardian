import json
import subprocess
import sys
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "textstats.py"


def run_cli(tmp_path, text, *args):
    input_file = tmp_path / "sample.txt"
    input_file.write_text(text)

    return subprocess.run(
        [sys.executable, str(SCRIPT), str(input_file), *args],
        capture_output=True,
        text=True,
    )


def test_basic_counts(tmp_path):
    result = run_cli(tmp_path, "Hello world\nSecond line\n")

    assert result.returncode == 0
    assert result.stdout == (
        "Lines: 2\n"
        "Words: 4\n"
        "Characters: 24\n"
    )


def test_counts_punctuation_as_word_separators(tmp_path):
    result = run_cli(tmp_path, "one, two! three?\n")

    assert result.returncode == 0
    assert "Lines: 1\n" in result.stdout
    assert "Words: 3\n" in result.stdout
    assert "Characters: 17\n" in result.stdout


def test_top_words(tmp_path):
    result = run_cli(
        tmp_path,
        "apple banana apple cherry banana apple",
        "--top", "2",
    )

    assert result.returncode == 0
    assert result.stdout == (
        "Lines: 1\n"
        "Words: 6\n"
        "Characters: 38\n"
        "Top 2:\n"
        "apple: 3\n"
        "banana: 2\n"
    )


def test_ignore_case(tmp_path):
    result = run_cli(
        tmp_path,
        "Apple apple APPLE banana",
        "--top", "2",
        "--ignore-case",
    )

    assert result.returncode == 0
    assert "apple: 3\n" in result.stdout
    assert "banana: 1\n" in result.stdout


def test_frequency_ties_sorted_alphabetically(tmp_path):
    result = run_cli(
        tmp_path,
        "pear apple banana",
        "--top", "3",
    )

    assert result.returncode == 0
    top_section = result.stdout.split("Top 3:\n", 1)[1]
    assert top_section == (
        "apple: 1\n"
        "banana: 1\n"
        "pear: 1\n"
    )


def test_min_length(tmp_path):
    result = run_cli(
        tmp_path,
        "a cat cat elephant elephant elephant dog",
        "--top", "3",
        "--min-length", "4",
    )

    assert result.returncode == 0
    assert "Words: 7\n" in result.stdout
    assert "elephant: 3\n" in result.stdout
    assert "cat:" not in result.stdout
    assert "dog:" not in result.stdout
    assert "a:" not in result.stdout


def test_min_length_and_ignore_case(tmp_path):
    result = run_cli(
        tmp_path,
        "CAT Cat elephant ELEPHANT elephant",
        "--top", "3",
        "--ignore-case",
        "--min-length", "4",
    )

    assert result.returncode == 0
    assert "elephant: 3\n" in result.stdout
    assert "cat:" not in result.stdout


def test_json_basic_counts(tmp_path):
    result = run_cli(
        tmp_path,
        "Hello world\nSecond line\n",
        "--json",
    )

    assert result.returncode == 0
    assert json.loads(result.stdout) == {
        "lines": 2,
        "words": 4,
        "characters": 24,
    }


def test_json_with_top_words(tmp_path):
    result = run_cli(
        tmp_path,
        "Apple apple banana banana banana",
        "--top", "2",
        "--ignore-case",
        "--json",
    )

    assert result.returncode == 0
    assert json.loads(result.stdout) == {
        "lines": 1,
        "words": 5,
        "characters": 32,
        "top": [
            {"word": "banana", "count": 3},
            {"word": "apple", "count": 2},
        ],
    }
def test_exclude_word_from_frequency_analysis(tmp_path):
    result = run_cli(
        tmp_path,
        "apple banana apple cherry banana apple date elderberry",
        "--top", "3",
        "--exclude", "apple",
    )

    assert result.returncode == 0

    # Exclusion does not change the overall word count.
    assert "Words: 8\n" in result.stdout

    # apple would normally be the most common word, but is excluded.
    assert "apple:" not in result.stdout

    top_section = result.stdout.split("Top 3:\n", 1)[1]

    assert top_section == (
        "banana: 2\n"
        "cherry: 1\n"
        "date: 1\n"
    )