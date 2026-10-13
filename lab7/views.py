from django.shortcuts import render

# Unordered collection -> a set (no guaranteed order, no duplicates)
FRUITS = {
    "Apple", "Banana", "Mango", "Orange", "Grapes",
    "Papaya", "Guava", "Pineapple", "Litchi", "Pomegranate",
}

# Ordered collection -> a list (index order is the selection order)
STUDENTS = [
    {"name": "Aarav Sharma", "roll_no": "BT21001", "branch": "CSE", "event": "Hackathon"},
    {"name": "Diya Verma", "roll_no": "BT21014", "branch": "CSE", "event": "Quiz"},
    {"name": "Kabir Singh", "roll_no": "BT21023", "branch": "IT", "event": "Hackathon"},
    {"name": "Meera Nair", "roll_no": "BT21030", "branch": "ECE", "event": "Debate"},
    {"name": "Rohan Gupta", "roll_no": "BT21042", "branch": "CSE", "event": "Quiz"},
    {"name": "Sneha Rawat", "roll_no": "BT21055", "branch": "IT", "event": "Debate"},
]

SORTABLE_FIELDS = {"name", "roll_no", "branch", "event"}


def fruits(request):
    """Task 7.1 + 7.3: unordered collection, empty-state alert, search."""
    query = request.GET.get("q", "").strip()
    items = list(FRUITS)
    if query:
        items = [f for f in items if query.lower() in f.lower()]
    # Shown in arbitrary set order on purpose; sorted only so output is stable.
    items.sort()

    # Demo switch for Task 7.1: /lab7/fruits/?empty=1 forces an empty list
    if request.GET.get("empty") == "1":
        items = []

    return render(request, "lab7/fruits.html", {"fruits": items, "query": query})


def students(request):
    """Task 7.1 (empty state), 7.2 (sorting), 7.3 (search)."""
    query = request.GET.get("q", "").strip()
    sort = request.GET.get("sort", "")
    direction = request.GET.get("dir", "asc")

    rows = list(STUDENTS)

    # Task 7.3: back-end search across all text fields
    if query:
        q = query.lower()
        rows = [
            s for s in rows
            if any(q in str(value).lower() for value in s.values())
        ]

    # Task 7.2: back-end sorting on a whitelisted field
    if sort in SORTABLE_FIELDS:
        rows.sort(key=lambda s: s[sort].lower(), reverse=(direction == "desc"))
    else:
        sort = ""

    next_dir = "desc" if (sort and direction == "asc") else "asc"

    context = {
        "students": rows,
        "query": query,
        "sort": sort,
        "direction": direction,
        "next_dir": next_dir,
        "total": len(STUDENTS),
    }
    return render(request, "lab7/students.html", context)
