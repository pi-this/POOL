import os

import subprocess




javaC = ''
win_title = "POOL"
width = 500
high = 500

w = str(width)
h = str(high)

ig = "pool.png"

def jre():
    os.system("sudo apt-get install default-jre >/dev/null 2>&1")
        
def jdk():
    os.system("sudo apt-get install default-jdk >/dev/null 2>&1")
    

    
def alert(text):
    
    java_code = (
        'import javax.swing.JOptionPane;\n\n'
        'public class Popup {\n'
        '    public static void main(String[] args) {\n'
        '        // Show a message dialog\n'
        '        JOptionPane.showMessageDialog(null, "' + text + '");\n'
        '    }\n'
        '}'
    )

    with open("popup.java", "w") as file:
        file.write(java_code)
        
    # Compile the Java file
    subprocess.run(["javac", "Popup.java"])
    
    # Run the Java class
    subprocess.run(["java", "Popup"])



class window:
    def open():
        global javaC
        global win_title
        global w, h, ig
        global width, high
        
        java_code = f"""
        import javax.swing.JFrame;
        import javax.swing.ImageIcon;
        import java.awt.Image;
        
        public class Window {{
            public static void main(String[] args) {{
                // Create a new frame (window)
                JFrame frame = new JFrame("{win_title}");

                // Set the size of the window (width, height)
                frame.setSize({width}, {high});
                
                // Load the image logo
                ImageIcon icon = new ImageIcon("{ig}"); // Replace with your image file path
                Image image = icon.getImage();
                
                // Set the window icon
                frame.setIconImage(image);

                // Specify what happens when the window is closed
                frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

                // Make the window visible
                frame.setVisible(true);
            }}
        }}
        """
            
     
        with open("Window.java", "w") as file:
            file.write(java_code)
        
        # Compile the Java file
        subprocess.run(["javac", "Window.java"])
    
        # Run the Java class
        subprocess.run(["java", "Window"])
        
    def setTitle(title):
        global win_title
        win_title = title
        
    def setSize(width,high):
        global w,h
        
        w = str(width)
        h = str(high)
        
    def setImage(img):
        global ig
        ig = img
        
    
        
