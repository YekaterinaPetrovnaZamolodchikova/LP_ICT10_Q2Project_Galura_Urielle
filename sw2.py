from pyscript import document

def compute_average(event):
    english = float(document.getElementById("english").value)
    math = float(document.getElementById("math").value)
    science = float(document.getElementById("science").value)
    ss = float(document.getElementById("ss").value)
    filipino = float(document.getElementById("filipino").value)
    ict = float(document.getElementById("ict").value)

    document.getElementById("english_output").innerText = english
    document.getElementById("math_output").innerText = math
    document.getElementById("science_output").innerText = science
    document.getElementById("ss_output").innerText = ss
    document.getElementById("filipino_output").innerText = filipino
    document.getElementById("ict_output").innerText = ict

    total = english + math + science + ss + filipino + ict
    average = total / 6

    first = document.getElementById("first").value
    last = document.getElementById("last").value

    document.getElementById("name").innerText = f"Name: {first} {last}"
    document.getElementById("output").innerText = f"Your General Weighted Average is {round(average, 2)}"

    document.getElementById("grades_container").style.display = "block"