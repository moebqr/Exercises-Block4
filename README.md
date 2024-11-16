## ST2195 Programming for Data Science

### Exercises 12 Nov 2024

**Exercise 1 (Guessing Game)** . Write a program in **both R and Python** that plays a guessing game. The program should generate a random integer number between 1 and 100. Then it should keep asking the user to guess the number, and give feedback after each trial whether the given number is bigger or smaller than the hidden one. The program should terminate when the user guesses the correct hidden number. Use seeding to randomize the choice of the hidden number. Use appropriate control structures such as looks and if statements.

**Exercise 2 (Times Table).** Write a program in both R and Python that prints the times table for the numbers from 1 to 12.

**Exercise 3 (Seconds Till Birth).** Write R and Python function that takes as argument the birth date (day, month, year) in Gregorian, then calculate and return the total number of seconds he/she lived till the current date and time.

I will not mark these unless you would like me to give you feedback. But it's better to practice git and pushing your solutions back to me in a new branch.


- Test your programs, then upload them to the repository on GitHub https://github.com/heshaaam/Exercises-Block4.git
- Here's how you can then upload your work on Github as another branch:

  - Clone the repository to your laptop:
    git clone https://github.com/heshaaam/Exercises-Block4.git
  - Change the directory to Exercises-Block4
    cd Exercises-Block4/
  - Make a branch with your student ID as the branch name. Assuming the ID is 20201234:
    git branch 20201234
  - Change the current branch from main to your ID number:
    git checkout 20201234
  - Add your files to the folder with the solutions. For example if you added a file named solution1.py do the following:
    git add solution1.py
  - Commit your solution file:
    git commit -m "Solution in Python to Exercise 1"
  - Push the changes (the file you added) to the branch you created:
    git push --set-upstream origin 20201234
  - Repeat the above for the six solution files. The files will appear as a branch with your ID its name under the repository.


