# Genetic Art 2
A second attempt at generating nice looking images in django using a genetic algorithm. This attempt will have a greater emphasis on testing and correctness before committing to github.

# Database Models

<b>Image<b>
 - Date/Time - date/time
 - Genome - bytestring
 - Generation - Int
 - Popularity - Int
 - Parents - Many-to-Many with Image

# To Do List

- <strike>0.5 - Start Django project.</strike>
- <strike>2 - write test cases for generator.py.</strike>
- <strike>0.5 - import svg.py in to this app.</strike>
- <strike>1 - write generator.py.</strike>
- 0.5 - write a view that shows an image generated from generator.py.
- 1 - write some test cases for Image models.
- 2 - write the Image model.
- 1 - write the admin panel code for Images.
- 1 - write a template and view for the frontend.
- 3 - write the javascript for the front end to send and receive choices/images.
- 2 - write the css for the frontend.
- 1 - write a view for getting family tree style information.
- 1 - upgrade the template and view to encorporate this family tree
- 2 - upgrade the javascript to fetch columns in the family tree when we submit choices.
- 2 - create a generation-view page, where you can view a generation without being able to make choices.
