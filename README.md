:warning: Everything between << >> needs to be replaced

# Math Around the World
## CS 110 Final Project
### Summer 2019
### [Assignment Description](https://docs.google.com/document/d/1d6wcXns0hz7HcUr4yF_tJK3QBx3daybmJO3dREPxABA/edit?usp=sharing)

https://github.com/binghamtonuniversity-cs110/final-project-sum19-joke
<< [link to demo presentation slides](#) >>

### Team: JOKe
#### Kimberly Meeker kmeeker2@binghamton.edu
#### Jae Kim jkim614@binghamton.edu
#### Yuqiao Huang yhuan171@binghamton.edu

***

## Project Description
(tentative) This is a math game called 'Math Around the World.' In this game, you will see math problems with increasing difficulties. Hurry up! They are dropping down! Do not let the problems touch the ground or else you lose the game. You will also have a chance to interact with cultural elements from China, Egypt, and Italy.

***    

## User Interface Design
* A wireframe or drawing of the user interface concept along with a short description of the interface. You should have one for each screen in your program.
    * For example, if your program has a start screen, game screen, and game over screen, you should include a wireframe / screenshot / drawing of each one and a short description of the components
    * You should also have a screenshot of your final GUI

***        

## Program Design
* You should have a list of any additional libraries or modules used (pygame, request) beyond non-standard python.
    * For each additional module you should include
        * url for the module documentation
        * a short description of the module
* Decide upon a class interface for the classes in your project.
    * A simple drawing that shows the class relationships in your code (see the sample Proposal document for an example). ![class diagram](assets/class_diagram.jpg)
    * This does not need to be overly detailed, but should show how your code fits into the Model/View/Controller paradigm.
* You should have a list of each of your classes with a description.

***

## Tasks and Responsibilities
* You must outline the team member roles and who was responsible for each class/method, both individual and collaborative.

### Software Lead - Yuqiao Huang (tentative)

<< Worked as integration specialist by... >>

### Front End Specialist - Jae Kim (tentative)

<< Front-end lead conducted significant research on... >>

### Back End Specialist - Kimberly Meeker (tentative)

<< The back end specialist... >>

## Testing
* Describe your testing strategy for your project.
    * Example

### Menu Testing

<< describe testing methods >>


### Game Testing

<< describe testing methods >>

* A copy of your ATP

| Step                  | Procedure     | Expected Results  | Actual Results |
| ----------------------|:-------------:| :-----------------| -------------- |
|  1  | Open terminal, navigate to the final project folder, and type 'python3 main.py' in the terminal.  | 'Math Around the World' starts and displays the Menu Screen. Background music plays.  |  |
|  2  | Left click on 'RULES' button.  | 'Math Around the World' displays the Rules Screen. Background music plays. | |
|  3  | Tap 'ESC' key.  | 'Math Around the World' goes back to the Menu Screen. Background music plays. | |
|  4  | Left click on 'START' button.  | 'Math Around the World' displays the Country Selection Screen with buttons for China, Egypt, and Italy. Background music plays. | |
|  5  | Left click on 'China' button.  | 'Math Around the World' displays a game screen with China-themed background, icons, and music. In the upper left corner, a Health Bar displays 3 Health Icons, which represent the number of times the user can fail before the game ends, and a ScoreBoard, which is initially set to 0 for regular game play and will be updated as the user earns points. At the bottom of the screen, there is a rectangle-shaped Answer Type-In Box for displaying the values typed by the user. Question Boxes with math problems begin descending from the top of the screen.  | |
|  6  | Type '100'.  | The number 100 appears in the Answer Type-In Box.  | |
|  7  | Tap 'BACKSPACE' key once.  | The final 0 will be removed from the number in the Answer Type-In Box, leaving '10'.  | |
|  8  | Press 'ENTER' key.  | The Answer Type-In Box clears. If 10 is the answer to the problem in the Question Box that is closest to the ground, the Question Box disappears and a chime sound plays. Otherwise, a buzzer sound plays, and the Question Box keeps falling. If a Question Box hits the ground before its correct answer is entered, a clunk sound plays and one Health Icon is removed from the Health Bar.  | |
|  9  |  Tap 'ESC' key.  | 'Math Around the World' goes back to the Menu Screen. Background music plays. | |
|  10  | Left click on 'START' button.  | 'Math Around the World' displays the Country Selection Screen with buttons for China, Egypt, and Italy. Background music plays. | |
|  11  | Left click on 'Egypt' button.  | 'Math Around the World' displays a game screen with Egypt-themed background, icons, and music. In the upper left corner, a Health Bar displays 3 Health Icons, which represent the number of times the user can fail before the game ends, and a ScoreBoard, which is initially set to 0 for regular game play and will be updated as the user earns points. At the bottom of the screen, there is a rectangle-shaped Answer Type-In Box for displaying the values typed by the user. Question Boxes with math problems begin descending from the top of the screen.  | |
|  12  | Type '-2.5'.  | The number -2.5 appears in the Answer Type-In Box.  | |
|  13  | Press 'ENTER' key.  | The Answer Type-In Box clears. If -2.5 is the answer to the problem in the Question Box that is closest to the ground, the Question Box disappears and a chime sound plays. Otherwise, a buzzer sound plays, and the Question Box keeps falling. If a Question Box hits the ground before its correct answer is entered, a clunk sound plays and one Health Icon is removed from the Health Bar. | |
|  14  |  Tap 'ESC' key.  | 'Math Around the World' goes back to the Menu Screen. Background music plays. | |
|  15  | Left click on 'START' button.  | 'Math Around the World' displays the Country Selection Screen with buttons for China, Egypt, and Italy. Background music plays. | |
|  16  | Left click on 'Italy' button.  | 'Math Around the World' displays a game screen with Italy-themed background, icons, and music. In the upper left corner, a Health Bar displays 3 Health Icons, which represent the number of times the user can fail before the game ends, and a ScoreBoard, which is initially set to 0 for regular game play and will be updated as the user earns points. At the bottom of the screen, there is a rectangle-shaped Answer Type-In Box for displaying the values typed by the user. Question Boxes with math problems begin descending from the top of the screen.  | |
|  17  | Type the correct answer to the problem in the Question Box that is closest to the bottom of the screen.  | The number typed appears in the Answer Type-In Box.  | |
|  18  | Press 'ENTER' key.  | The Answer Type-In Box clears. The Question Box disappears and a chime sound plays. The ScoreBoard is updated. | |
|  19  | Allow a total of 4 Question Boxes to hit the ground.  | 'Math Around the World' displays Game Over and shows the user's score.  | |
|  20  | Left click on 'Play Again' button.  | 'Math Around the World' goes back to the Menu Screen. Background music plays.  | |
|  21  | Left click on 'CREDITS' button  | 'Math Around the World' displays credits and acknowledgements on the screen.  | |
|  22  | Tap 'ESC' key.  | 'Math Around the World' goes back to the Menu Screen.  | |
|  23  | Tap 'ESC' key.  | 'Math Around the World' closes.  | |
