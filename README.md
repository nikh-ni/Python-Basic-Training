1. 步驟一：在 GitHub 建立一個新的 Repository（倉庫）
2. 步驟二：在你的電腦上準備好檔案
3. 步驟三：初始化 Git 版本控制
git init
git add .
git commit -m "First upload:Basic Python Training" #新增備註
4. 步驟四：連結到 GitHub Repository
git remote add origin https://github.com/你的帳號/python-practice.git
git branch -M main
git push -u origin main
5. 步驟五：完成上傳！在網頁上檢查看看

6. 修改commit
git commit --amend -m "First upload: added hello.py"
git push --force

7. 上傳修改檔案
git add Upload.py
git commit -m "修改檔案"
git push
