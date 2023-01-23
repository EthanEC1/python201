courses = {
    "js": "JavaScript 101",
    "python": ["Python 101", "Python 201"],
    "html": "HTML 101",
    "css": "css 101"
}

print(courses.get("css", "css 101"))
if courses.get("css", "css 101"):
    print("You are enrolled in CSS 101")