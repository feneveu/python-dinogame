Dino Game in pygame

I attempted building a dino game in pygame which came out fairly well laid out,
I did find it hard finding good dino images on the internet. I cropped images and
had weird functionality in my dino movement. This is when I realized I wanted to 
find a better looking version/layout so I went to github. I found a fantastic version
that had all of the images premade for me. I built those into my game and then I 
realized from there that for all the work I could do my game would never look right

I realized that utilizing the resources around me would make me a better coder so I
walked line by line through the code given by:

https://www.youtube.com/watch?v=jm-VFy_03DQ
https://github.com/tuffleroot/chrome-dino-pygame/tree/master

I learned a lot from this walk through. In my original code, I had brute forced the
concept of "sprites" 
I had a current image that was the dino position and it would flip back and forth per tick
            if dino_image == current_image:
                current_image = dino_image2
            else:
                current_image = dino_image

The sprite technique had a list that would iterate through the images of each sprite
and it allowed me easy access to sprite collisions

From there it was incredibly userful to learn about pygame masking which created a
more indepth pixel collision map

Again it is always fun to think about the physics in the game, using dt as the change
in time and that has to be multiplied by speed and then when dealing with the jump
the gravity of the sprite has to be taken into account

It was also very interesting to watch how the different sprites move around the dino,
each individual sprite had speed/movements while the dino stayed in place

Overall this was such an informative project, I completely understand the ins and outs
of all of the lines of code and I am confident that I could implement a sprite in motion

Again in my first verion, I was able to have an image built on a rect that had collisions
with cacti that moved towards it, the other version game me a more professional look on the 
coding problem



