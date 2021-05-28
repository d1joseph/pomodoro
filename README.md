# A Simple pomodoro timer
I'm making my own pomodoro timer to use for my daily productivity stuff. I'll be using PySimpleGUI and the time standard libraries for version 0.

Here's a rough functional idea of what version 0 should look like...
![Huy's Pomodoro](ui/huys-pomodoro.png)

And where I'm aiming to get to in the first iteration.

### version 1.0
![Huy's Pomodoro](ui/huyp-beta-main.svg)

### version 1.0
Task creation view
![Huy's Pomodoro](ui/huyp-beta-task-create-view.svg)

HuysPomodoro app is composed of 7 widgets;
1. A task queue widget with latest task emphasised.
2. A time feed with active/break/paused/rested time states.
3. A neuro activity graph metric if the user connects any neural tech wearable devices via bluetooth.
4. Daily activity health markers if the user connects any health tracking wearable devices via bluetooth.
5. A key productivity rating measure averaged during a session.
6. Controls - Go, Stop and Next buttons.
7. Application settings.

# Just a really nice desktop productivity app
I wanted to build something I could use everyday in my own life and I wanted it to be high performant, functional, simple and yet
let's me take advantage of modern engineering and digital design to craft something cool. 

## To do:
* <s>Finish v1 designs</s>
* write logic and app component modules
* write unit test fixtures and test with pytest
* test/debug
* compile binaries and package for installation
* deploy
