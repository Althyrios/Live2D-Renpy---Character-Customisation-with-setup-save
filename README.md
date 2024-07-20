# Live2D-Renpy -Character Customisation with setup save

Hello,
This template / tutorial is for Renpy developers who want to use the Live2D plugin to animate characters in their game.
The following scripts allow you to create sets of clothes to equip and unequip. The same applies to the physical aspects of your characters (visible or invisible reddening or scars).

## Step 1 : Install Live2D Cubism

Download Live2D Cubism and install the Renpy plugin.
Create your own character or use one you've already made.
Follow this tutorial to learn the basics of the software and how to use it on Renpy (thanks to Visual Novel Design for this wonderful tutorial) https://www.youtube.com/watch?v=xwW8Plpz1RQ

## Step 2 : Prepare your character

### Parameters

Once you've drawn or imported your character, rigging it as explained in the youtube tutorial.
Then create the parameters you'll use to animate your character.

Note 1: The Live2D Cubism physics system is not currently supported by Renpy, unlike Unity. You can still link the movement of hair or clothing to one or more specific sliders (e.g. hair moves when neck or torso sliders are moved).

To create our skinning system, we'll need additional sliders, or “visibility sliders”.
For example, if you have several haircuts, create a “hair_visibility” slider. In 0, all haircuts will have an opacity of 0%; in 1, haircut 1 will have a visibility of 100% and the others of 0%; in 2, haircut 2 will have a visibility of 100% and the others of 0%, and so on.

Note 2: It's advisable to make the visibility sliders before the others, to ensure that the elements are visible or invisible, whatever position the body adopts.

Note 3: Make sure that the DEFAULT position of your parameters is correctly set.

DON'T FORGET to generate the Atlas texture and export it

### Animations

Create as many animations as you like, making sure your visibility slider is correctly set.
I recommend that you leave visibility sliders at 0 when exporting animations.

### Live2D Viewer

Open live2D viewer and open your character's Live2D file (the .moc3 file NOT the animation file).

Now you can create all your character's “expressions”.
Contrary to what the name suggests, you can also use expressions to dress up your character.
So, if you have 3 haircuts you'll need to create 3 different expressions, “haircut_1_on”, “haircut_2_on”, “haircut_3_on”.
For each expression, choose the positions of the different Parameters that will be linked to that expression.

![image](https://github.com/user-attachments/assets/3b4e471d-609e-4cf2-94f1-b580ff4abe17)

You can choose as many parmaeters as you want to create the face expressions but I recommand you to use only one or two parameters for "body" and "clothes" expression that will be equip on the character.

Then click on expprt to export the model, the expressions and the poses.

## Step 3: Renpy

Create the a folder for each characters inside /images/characters
Each folder must contain :
- The texture atlas of the chracter in its own folder created when exported from Live2D
- The poses .motion3 files
- The expressions .exp3 files
- The main file of your character .moc3
- A model file .model3
- A .cdi3 file

Then you can use the classes and functions from this repo to make your own animated character in your Renpy project with customisation

## Step 4: Feedback and "What's not here"

Do not hesitate to give me some feedback, what you didn't understand, what you think is not clear enough... Create a new "Issue"

The code here is NOT using any lipsync or facial expression because I don't use them for now, this will be added in a future update.

In the future I will add a character in this repo so anyone could test it on renpy.


