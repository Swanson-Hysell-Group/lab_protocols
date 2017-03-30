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
