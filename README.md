## Flask Application Design

### HTML Files
- **home.html:** This file will serve as the landing page for the game. It will include visually stunning images, engaging animations, and concise, captivating text to effectively showcase the game's features and appeal to potential players. The color scheme will be inspired by the Dune universe, featuring deep blues, rich oranges, and sandy neutrals. All animations will be smooth and not overly distracting from the content. High-quality images of the game components, artwork, and thematic elements will be used throughout the page.
- **about.html:** This file will provide additional information about the game, such as its history, gameplay, and setting. It will include detailed descriptions and engaging visuals to immerse the players in the world of Dune: Imperium.
- **contact.html:** This file will include a form for players to contact the game's creators or ask any questions. It will also provide contact information for the development team.

### Routes
- **@app.route("/")**: This route will handle the rendering of the home page, "home.html".
- **@app.route("/about")**: This route will handle the rendering of the about page, "about.html".
- **@app.route("/contact")**: This route will handle the rendering of the contact page, "contact.html".
- **@app.route("/submit_form", methods=['POST'])**: This route will handle the form submission from the contact page and process any data entered by the user.