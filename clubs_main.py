from pyscript import document

clubs_data = {
    "dance": {
        "name": "Dance Club",
        "description": "The Dance Club is a vibrant community where students explore various dance styles including hip-hop, contemporary, and traditional dances. Members showcase their talents in school events and competitions.",
        "meeting_time": "Every Tuesday and Thursday, 3:30 PM - 5:00 PM",
        "location": "School Gymnasium",
        "teacher": "Ms. Chloe Galope",
        "members": 16,
        "category": "Non-Academic"
    },
    "cooking": {
        "name": "Cooking Club",
        "description": "The Cooking Club brings together food enthusiasts who learn culinary skills and cultural cuisines. Members prepare delicious dishes and participate in cooking competitions and school events.",
        "meeting_time": "Every Wednesday and Friday, 4:00 PM - 5:30 PM",
        "location": "School Kitchen",
        "teacher": "Mr. Andrei Tecson",
        "members": 13,
        "category": "Non-Academic"
    },
    "literature": {
        "name": "Literature Club",
        "description": "The Literature Club is dedicated to the appreciation and study of literature. Members engage in book discussions, creative writing, poetry readings, and literary analysis to enhance their communication and critical thinking skills.",
        "meeting_time": "Every Monday and Wednesday, 3:30 PM - 4:45 PM",
        "location": "School Library",
        "teacher": "Ms. Korinne Reyes",
        "members": 12,
        "category": "Academic"
    }
}

def show_club_info():
    selected_club = document.getElementById("club-dropdown").value
    
    if selected_club == "":
        document.getElementById("club-info").style.display = "none"
        return
    
    club = clubs_data[selected_club]
    
    document.getElementById("club-name").innerText = club["name"]
    document.getElementById("club-description").innerText = club["description"]
    document.getElementById("club-meeting").innerText = club["meeting_time"]
    document.getElementById("club-location").innerText = club["location"]
    document.getElementById("club-teacher").innerText = club["teacher"]
    document.getElementById("club-members").innerText = club["members"]
    document.getElementById("club-category").innerText = club["category"]
    
    document.getElementById("club-info").style.display = "block"
