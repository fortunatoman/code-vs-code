# Git Rebase Challenge

You’re given a basic calculator project with two feature branches.  
The goal is to **rebase** both features onto `main` with a clean, linear history.

---

## 🧱 Branches

- `main`: Basic calculator with **addition**
- `feature-subtraction`: Adds **subtraction**
- `feature-multiplication`: Adds **multiplication**

---

## ✅ Final Result

 - Run `git log` on `main` and it should look like:
```
<commit-hash-3> feat: add multiplication
<commit-hash-2> feat: add subtraction
<commit-hash-1> feat: initial calculator with addition
```
---
No merge commits. No branching.

---

## 🚀 Steps

1. **Fork** this repo to your GitHub account  
2. **Clone** your fork  
   ```bash
   git clone https://github.com/<your-username>/<repo-name>.git
   cd <repo-name>
 - ⚠️ **Important**: Create Pull Requests to your forked repository only. Do not create PRs to the original repository.

3. Create a pull request from `feature-subtraction` to `main`  
   → Use Rebase and Merge
4. Create a pull request from `feature-multiplication` to `main`  
   → You'll hit conflicts, resolve them
   → Use Rebase and Merge

---
Send a link to your forked repo when you're done.