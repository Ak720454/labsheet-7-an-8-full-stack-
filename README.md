# BTCS303P: Django Lab Sheets 7 & 8

One Django project covering both lab sheets.

| Task | Where |
|------|-------|
| 7.1 Empty-state alert (`{% if %}`) | `templates/lab7/fruits.html`, `students.html` (try `/lab7/fruits/?empty=1`) |
| 7.2 Table sorting by field | `lab7/views.py` `students()` + header links in `students.html` |
| 7.3 Search form (back-end filtering) | `lab7/views.py` (`q` GET param) |
| 8.1 Active nav highlighting | per-link `{% block nav_* %}` in `templates/base.html` |
| 8.2 Persistent message box | `{% block messages %}` in `base.html` + Django messages framework |
| 8.3 Contact Us form -> server logs | `lab8/forms.py`, `lab8/views.py`, `LOGGING` in `config/settings.py` |

## Run

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py runserver
```

Open http://127.0.0.1:8000/

- Home / About / Contact: `/`, `/about/`, `/contact/`
- Fruits: `/lab7/fruits/`
- Students: `/lab7/students/` (click column headers to sort, use the box to search)

Submitting the Contact form prints a `CONTACT FEEDBACK | ...` line in the terminal
and appends it to `logs/contact.log`.

No database models are used, so `migrate` is optional (it only sets up session tables).
Run `python manage.py migrate` once if you see a sessions-table error when submitting the form.
