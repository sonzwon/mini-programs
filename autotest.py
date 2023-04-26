import tkinter as tk
import tkinter.messagebox
import os
import fileinput
import sys



class Application(tk.Frame): 
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.master = master
        self.file = "test3.py"
        self.check_file(self.file)
        self.UI()
        


    def UI(self):
        self.auto_button = tk.Button(self, 
                                     text="AUTO",
                                     width=30,
                                     height=15,
                                     overrelief="solid",
                                     relief="ridge",
                                     bg="yellow",
                                     command=lambda: self.auto_btn())
        self.auto_button.place(x=50, y=70)

        self.manual_button = tk.Button(self, 
                                     text="MANUER",
                                     width=30,
                                     height=15,
                                     overrelief="solid",
                                     relief="ridge",
                                     bg="yellow",
                                     command=lambda: self.manual_btn())
        self.manual_button.place(x=350, y=70)



    def check_file(self, file):
        """파일 찾기"""
        # 첫번째 폴더 경로
        dir_1 = "./base"
        # 두번째 폴더 경로
        dir_2 = "./others"

        for dir in [dir_1, dir_2]:
            if os.path.exists(dir + "/" + file): #파일 찾기
                os.chdir(dir)       # 파일 있으면 디렉터리 변경
                print(f"pwd : {dir}")
                if self.auto_true():  # 파일 안에 auto=True 찾기
                    print(f"{self.file} : auto = True")
                else:
                    print(f"{self.file} : auto = False")




    def auto_true(self):
        """파일 내 auto = True 찾기"""
        with open(self.file, "r") as f:
            lines = f.readlines()
        f.close()
        for line in lines:
            if 'auto = True' in line:
                return True
        return False



    def auto_btn(self):
        """auto 버튼 실행"""
        if self.auto_true():
            self.auto_button.configure(bg="green")
            if tkinter.messagebox.askokcancel("Complete", "Complete !"):
                root.destroy()

        else:
            try:
                self.update_file()
            except:
                print("disavailable")

            self.auto_button.configure(bg="green")
            if tkinter.messagebox.askokcancel("Complete", "Complete !"):
                root.destroy()


    
    def manual_btn(self):
        """manual 버튼 실행"""
        if self.auto_true():
            try:
                self.update_file()
            except:
                print("disavailable")

            self.manual_button.configure(bg="green")
            if tkinter.messagebox.askokcancel("Complete", "Complete !"):
                root.destroy()
        
        else:
            self.manual_button.configure(bg="green")
            if tkinter.messagebox.askokcancel("Complete", "Complete !"):
                root.destroy()

    
    def update_file(self):
        for line in fileinput.input(self.file, inplace = True):
            if "auto = True" in line:
                line = line.replace(line, "auto = False")
            elif "auto = False" in line:
                line = line.replace(line, "auto = True")
            
            sys.stdout.write(line)





if __name__ == "__main__":
    root = tk.Tk()
    root.title("Check")
    root.geometry("640x400+650+300")
    root.resizable(False, False)
    Application(root).pack(side="bottom", fill="both", expand=True)
    root.mainloop()