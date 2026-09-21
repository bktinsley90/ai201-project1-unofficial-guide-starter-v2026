# Acceptance criteria — The Unofficial Guide

Five criteria that say what "working" means for this system, written in unit 1
**before** any results existed.

An acceptance criterion names a target: a number, a count, a rate, or something
a person could plainly observe. *"Retrieval works"* is an opinion. *"For at
least 4 of my 5 test questions, the top results include a chunk containing the
answer"* is a criterion.

Under each one, write a sentence or two on **why that target** and not a
stricter or looser one. A reason that says something about your corpus or your
pipeline earns credit; *"80% seemed reasonable"* does not.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## 1. Retrieved chunks contain the answer

For at least 4 of my 5 test questions, the retrieved chunks include one that
contains the answer.

**Why this target:**

I chose 4 of 5 because the advice threads contain several replies, and useful
information can be spread across a chunk boundary. Most questions should still
retrieve the relevant reply, but allowing one miss reflects the messier shape
of this corpus.

---

## 2. Every answer names a source

Every answer the system produces names at least one source document.

**Why this target:**

I chose all five because the answer prompt explicitly tells the model to name
the filename used, and every retrieved chunk includes its source metadata. An
answer would miss this target only if the model ignored the instruction or the
source information were lost before generation.

---

## 3. The relevance gate stops out-of-corpus questions

When I ask a question my documents clearly don't cover, the relevance gate
stops it and the system returns "I don't have enough information about that" —
in at least 4 of 5 tries.


**Why this target:**

I chose 4 of 5 because the out-of-scope questions are clearly unrelated to
college advice, so the relevance gate should refuse most of them using the
0.60 cutoff. Allowing one miss accounts for the possibility that an unrelated
question could still produce a misleadingly close embedding match.

---

## 4. Something about your chunks


For all 5 of my test questions, the system retrieves no more than 3 chunks,
and every retrieved chunk has a similarity score above 0.70.

**Why this target:**

The advice-thread corpus contains short discussions with answers spread across
multiple replies, so limiting retrieval to three focused chunks should provide
enough context without adding unrelated replies. A similarity score above 0.70
sets a consistent quality bar for the retrieved context.


---

## 5. Your choice

For at least 4 of my 5 test questions, the generated response answers the
prompt in 3 sentences or fewer without omitting key factual details from the
retrieved chunk.

**Why this target:**

Students asking these questions need practical answers that are quick to read,
while the response still needs to preserve important details such as costs,
timing, or recommended actions from the source thread.


---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 2 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath it, like this:

         ## 1. Retrieved chunks contain the answer

         For at least 4 of my 5 test questions, the retrieved chunks include
         one that contains the answer.

         **Why this target:** ...

         > **Revised in unit 2:** For at least 4 of 5 questions, the top three
         > results contain the answer.
         >
         > **Why revised:** I couldn't judge "the chunks include one that
         > contains the answer" the same way twice — I scored two questions
         > differently on Monday than on Wednesday. The new version is
         > something I can actually check.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "I said 4 of 5 but got 2 of 5, so 2 of 5 is more realistic."

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.

     The whole reason the originals stay visible is so someone can see what you
     said before you knew the answer.
     ───────────────────────────────────────────────────────────────────────── -->
