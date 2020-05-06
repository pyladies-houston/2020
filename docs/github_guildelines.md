## Issue Titles

- Issues that add features should begin with the word "Add".

## Commit Messages

See:

- https://chris.beams.io/posts/git-commit/
- https://gist.github.com/robertpainsi/b632364184e70900af4ab688decf6f53
- https://github.com/erlang/otp/wiki/Writing-good-commit-messages/60609c92910b881178742855502957bf18cdd00a

To create the best experience for viewers of history in various tools:

- First line stops at 50 characters.
- Blank line.
- Remaining lines wrap at 72 characters.

```
         1         2         3         4         5         6         7
12345678901234567890123456789012345678901234567890123456789012345678901234567890
                                                 X                     X
```

This puts severe constraints on branch names if the commit summaries are to be meaningful.

## Branch Names

- Limit to 42 characters
- Format: `issue-{num}/{verb}_{remainder}`
- Verb can be:
    - add
    - fix
    refactor
- If len(str(num)) == 3 and verb == "add", then len(remainder) <= 38

## PR

### PR Title

`{branch_name}`

### PR Body

Proposal for what goes into the commit message after the title.

### PR Commit Messages

- `PR #{num} {branch_name}`
- Blank line
- See https://chris.beams.io/posts/git-commit/
- Optional tags at end:
    - "Resolves": for _additional_ issues that were also resolved by the PR
    - "See also": if needed, for things like epics and related issues

### Merging

- The person who is assigned should do the merge.
- If nobody is assigned, then the author should do the merge.
- The merge should be a standard non-fast-forward merge, not squash or rebase.
- A PR should have a commit message that explains what and why. This can take time.
- It should always be a non-fast-forward merge commit.
- After merge, any connected issues should be:
    - closed if there is nothing more to do
    - annotated if there is more work to do
- Finally, delete the associated branch. (You can always restore from the closed PR.)
