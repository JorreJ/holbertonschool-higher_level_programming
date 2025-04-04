# JavaScript DOM Manipulation

A series of hands-on JavaScript exercises focused on learning and practicing DOM manipulation, event handling, and basic network requests using `fetch`.

## 📚 Resources

Before diving into the scripts, you may want to check out the following references:

- [What is JavaScript?](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- [Introduction to the DOM](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Introduction)
- [Document Interface](https://developer.mozilla.org/en-US/docs/Web/API/Document)
- [Element Class](https://developer.mozilla.org/en-US/docs/Web/API/Element)
- [CSS Selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Selectors)
- [Play CSS Diner](https://flukeout.github.io/)
- [DOM Scripting](https://www.w3schools.com/js/js_htmldom.asp)
- [Using Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API)
- [Troubleshooting JavaScript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/What_went_wrong)

---

## 🎯 Learning Objectives

By the end of this project, you should be able to:

- Select HTML elements using JavaScript
- Distinguish between ID, class, and tag selectors
- Modify HTML content and style dynamically
- Update and traverse the DOM
- Make asynchronous requests with `XMLHttpRequest` and `fetch`
- Handle DOM and user events

---

## ⚙️ Requirements

- ✅ Code is compatible with Chrome 57+  
- ✅ No usage of `var` (use `const` or `let`)  
- ✅ All files end with a newline  
- ✅ DOM manipulation only (no page reloads)  
- ✅ Follow [semistandard](https://github.com/standard/semistandard) JavaScript style  

---

## 📁 Project Structure

```
javascript-dom_manipulation/
├── 0-script.js            # Change header color using querySelector
├── 1-script.js            # Change color on click
├── 2-script.js            # Add a class on click
├── 3-script.js            # Toggle classes red/green
├── 4-script.js            # Add list item to <ul> on click
├── 5-script.js            # Update header text on click
├── 6-script.js            # Fetch and display a Star Wars character
├── 7-script.js            # Fetch and display all Star Wars movies
├── 8-script.js            # Display 'Hello' in French from API
├── *.html                 # Test HTML files for each script
└── README.md              # Project documentation
```

---

## 🧪 Tasks Overview

- Task 0 : updates the text color of the `header` element to red
- Task 1 : updates the text color of the `header` element to red when the user clicks on the tag with id `red_header`
- Task 2 : adds the class `red` to the `header` element when the user clicks on the tag with id `red_header`
- Task 3 : toggles the class of the `header` element when the user clicks on the tag id `toggle_header`
  * User can toggle between `green` and `red`
- Task 4 : adds a `li` element to a list when the user clicks on the element with id `add_item`
  * The new element will be `<li>Item</li>` and will be added to the `ul` element with class `my_list`
- Task 5 : updates the text of the `header` element to "New Header!!!" when the user clicks on the element with id `update_header`
- Task 6 : fetches the character `name` from this URL : https://swapi-api.hbtn.io/api/people/5/?format=json
  * The name will be displayed in the HTML tag with id `character`
- Task 7 : fetches and lists the `title` for all movies by using this URL : https://swapi-api.hbtn.io/api/films/?format=json
  * All movie titles will be listed in the HTML `ul` element with id `list_movies`
- Task 8 : fetches and displays the value of `hello` from this URL : https://hellosalut.stefanbohacek.dev/?lang=fr
  * The translation of “hello” must be displayed in the HTML element with id `hello`
  * The script work when it is imported from the `<head>` tag

---

## 🔧 How to Run

1. **Clone the repository**:
   ```bash
   git clone https://github.com/holbertonschool-higher_level_programming.git
   cd holbertonschool-higher_level_programming/javascript-dom_manipulation
   ```

2. **Open any HTML test file** (e.g., `0-main.html`) in your browser to see the script in action.

3. **Interact** with the elements (buttons, headers, etc.) to observe the DOM manipulations.

---

## 👤 Author

**Your Name**  
GitHub: [@yourusername](https://github.com/yourusername)  
Project developed as part of the Holberton School curriculum.

---

## 🪪 License

This project is licensed under the [MIT License](LICENSE).