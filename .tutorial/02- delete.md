# Cookies! Cookies!

Sessions are effectively cookies on the user's computer. So, we really need a way to delete them too.

👉 I'm going to create a button that forwards us to a page to do that. Here's the form code with the extra button. Update the code in 'form.html' in your file tree to match the code below:


```html
<form method="post" action="setName">
  <p>Name: <input type="text" name="name"></p>
  <button type="submit">Submit</button>
  <button type="button" onclick="location.href='/reset'">Reset</button>
</form>

```

## Reset
👉 Next, let's build the 'reset' page.  I've used `session.clear()` to clear the session (deletes all the stored data) and included a redirect to send us back to the main page.

```python
@app.route("/reset")
def reset():
  session.clear()
  return redirect("/")

```

### Remember to open the site in a separate tab to test if it is working properly.