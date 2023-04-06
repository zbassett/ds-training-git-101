# Answer Key: Git 101 Training - Flask App Breakout Session

## 1. Fork this repo
- Click the "Fork" button on the top-right corner of the original repository page.

## 2. Clone the forked repo
- Copy the URL of your forked repository.
- Open a terminal and run `git clone <your-forked-repo-url>`.

## 3. Navigate to the cloned directory
- In the terminal, run `cd <repo-name>`.

## 4. Instantiate flask app with a `docker run ...` command
- Make sure Docker is installed and running on your machine.
- Run `docker build -t flask-app ./flask_app` to build the Docker image.
- Run `docker run -d -p 5000:5000 --name flask-app flask-app ` to start the Flask app in a Docker container.

## 5. Confirm that the app is running by navigating to it with your web browser
- Open your web browser and go to `http://{YOUR_MACHINES_IP}:5000`. You should see a generated insult.

## 6. Update source code: add another adjective to the insult
- Open `app.py` with your favorite text editor.
- Add a new adjective:
```
    adjective1 = random.choice(adjectives)
    adjective2 = random.choice(adjectives)
    adjective3 = random.choice(adjectives)
    noun = random.choice(nouns)

    insult = f"You are a {adjective1}, {adjective2}, {adjective3} {noun}!"
```

## 7. Create a feature branch
- In the terminal, run `git checkout -b feature/add-adjective`.

## 8. Commit your change to the feature branch
- Run `git add app.py`.
- Run `git commit -m "Add new adjective to insult"`.

## 9. Push to the remote repository
- Run `git push origin feature/add-adjective`.

## 10. Create a pull request
- Go to your forked repository on GitHub.
- Click on the "Pull requests" tab and then click "New pull request".
- Choose the `main` branch as the base and your `feature/add-adjective` branch as the compare branch.
- Click "Create pull request" and add a title and description if necessary.

## 11. Merge into `main`
- On the pull request page, click "Merge pull request" and confirm the merge.

## 12. Clean up by deleting the feature branch
- On the pull request page, click "Delete branch" to remove the feature branch.
- In your terminal, switch back to the `main` branch with `git checkout main`.
- Run `git pull origin main` to update your local `main` branch with the latest changes.
- Finally, delete the local feature branch with `git branch -d feature/add-adjective`.