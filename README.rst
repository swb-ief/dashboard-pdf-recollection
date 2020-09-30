## Dashboard PDFs

We have recollected this PDFs from the github pipelines and others collected manually by members of the team.

Script executed to create PDFs for actual date:

```
ls *.pdf | xargs -L1 python ./move_file_with_first_page_date.py
```
