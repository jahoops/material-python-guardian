# Problem-Solving Process

This is a living collection of problem-solving principles and questions learned
from experience.

It is not a checklist, workflow, or required sequence. Use whatever is relevant.
Do not let the process interfere with productive exploration.

## Validate the payoff

- If this problem were solved perfectly, would the outcome actually matter?
- Is the underlying need still real?
- What concrete benefit would success produce?
- Am I solving the real problem, or a stale or intermediate problem?

## Distill the real need

- State what the solution MUST accomplish, not how it should accomplish it.
- Challenge every apparent requirement.
- Is this truly necessary for the outcome?
- Is it merely inherited from the first imagined solution?
- Remove assumptions about implementation, architecture, material, quantity,
  orientation, mechanism, or relationship unless they are genuinely required.
- Keep redistilling as new ideas reveal better understanding of the problem.

## Use solutions to learn about the problem

- Starting with a solution-shaped idea is acceptable.
- Treat candidate solutions as probes into the requirements.
- Ask why each part of the proposed solution is needed.
- If a proposed solution feels wrong, identify exactly what is wrong rather than
  rejecting it vaguely.
- Make backtracking cheap and early.

## Find what is already solved

- Has this outcome already been solved?
- More importantly: which PARTS of this problem have already been solved?
- What mature systems, products, mechanisms, libraries, materials, or techniques
  already provide the needed capabilities?
- Search by required capability, relationship, and interface rather than by the
  imagined product name.

## Analyze near-fit solutions

- If an existing solution worked perfectly as designed, what would still be missing?
- Which exact requirement does it fail?
- Can that specific gap be repaired rather than replacing the whole solution?
- Can a small custom interface adapt an otherwise mature solution?

## Build only the unsolved remainder

- Import mature capabilities instead of recreating them.
- A custom overall solution does not imply that every component should be custom.
- Decompose until the genuinely unique unsolved part is visible.
- Custom-build only the irreducible remainder.

## Let requirements choose tools and materials

- Do not start from the tools or materials available.
- First determine the required physical or functional properties.
- Then consider tools, materials, fabrication methods, software, or other
  capabilities that fit those requirements.
- Ignore solution branches that are obviously poor fits.
- Availability affects cost, time, and effort after promising solution families
  have been identified.

## Test assumptions cheaply

- Which assumptions can be tested instead of debated?
- Prefer measurements, searches, sketches, calculations, small experiments, and
  prototypes before expensive commitment.
- Do not evaluate strange ideas prematurely if a cheap test can clarify them.

## Learn from outcomes

- What worked?
- Under what conditions did it work?
- Why did it work?
- What failed?
- Why did it fail?
- What should not have to be rediscovered next time?
- What reusable pattern can be extracted from this success or failure?
- Does a pattern from previous work apply to the current problem?

## Preserve freedom

- The process serves the problem solvers; it does not command them.
- There is no mandatory order.
- Productive thought experiments and exploration should not be interrupted by
  procedural housekeeping.
- Questions may be ignored when irrelevant.
- The purpose of the doctrine is to restore valuable ways of thinking that might
  otherwise be forgotten.

  If this worked perfectly, would the result actually matter?

Is the underlying problem still real?
What are the true MUST requirements?
Which apparent requirements are inherited implementation assumptions?
Has this already been solved?
Which parts have already been solved?
If a near-fit solution worked perfectly as designed, what would still be missing?
Why exactly does the near-fit solution fail?
Can that gap be repaired rather than rebuilding everything?
Is there an assumption we can test cheaply?
What mature capability can we import?
What worked before, under what conditions, and can it be reused?
What failed, and why?
What general pattern can be extracted from a success?

ABSTRACT THIS: Strip away the incumbent implementation. State the required outcome and hard constraints. Identify unconstrained dimensions. Generate several different relational framings. Ask what mature systems in unrelated domains already implement those relationships. Look for intrinsic distinguishing properties and combinations of weak filters. Identify any assumptions that can be tested cheaply. Import existing capabilities before inventing mechanisms. Do not evaluate strange ideas prematurely.