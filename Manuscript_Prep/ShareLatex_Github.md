# Syncing a manuscript between ShareLatex and Github

Summary: avoid editing the same file concurrently on sharelatex and your local computer.

## To make changes on your local .tex file:

If you want to make changes on your local .tex file (or any file that has been edited within ShareLatex), here is the preferred protocol to avoid a mess of git conflicts:

1) commit and push changes made in sharelatex
2) pull changes on your local computer
3) make changes on your local computer
4) commit and push changes made on your local computer
5) pull changes into sharelatex
6) continue working in sharelatex

## To make changes on your local non-.tex files:

If you want to make changes on your local computer to files that have NOT been edited within ShareLatex (e.g. figures):

1) pull changes on your local computer (to make sure you are up to date with the Github master branch)
2) make changes to the files
3) commit and push changes made on your local computer
4) pull changes into sharelatex
5) continute working in sharelatex

Notes:
* committing and pushing changes made in sharelatex prior to making edits to non-.tex files is not required
* a author may continue to work on the sharelatex .tex while another author is making edits to non-.tex files on their local computer

## Important note on renaming files:

### The problem

ShareLatex does not like it when you rename files (or move them) on your local computer. Example of the problem:

1) rename a file on your local computer
2) push changes to Github from your local computer
3) pull changes into ShareLatex
4) make edits to your .tex in ShareLatex
5) push changes to Github from ShareLatex
6) pull changes onto your local computer

You may find that step 6 reverts changes that you made in step 1. This is because step 3 does not complete as expected in ShareLatex. ShareLatex will pull all changes made on your local computer EXCEPT changes that involve renaming/moving files. Therefore, when you perform step 5, ShareLatex will push the outdated versions of renamed files to Github, and so when you perform step 6, you will pull the outdated versions of renamed files.

### The solution

1) perform steps 1-3 above
2) MANUALLY rename files in ShareLatex to the new file names you created in step 1 - you can do this using the directory tree in the left panel
3) If you moved files, MANUALLY delete the file from its original directory and re-upload it to the new directory
4) push changes to Github from ShareLatex
