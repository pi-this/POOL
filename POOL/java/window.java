import javax.swing.JFrame;
import java.io.*;
import javax.swing.*;  
import java.awt.*; 
 
public class window{
  public static void main(String[] args){
    JFrame frame = new JFrame();
    int w = Integer.parseInt(args[1]);
    int h = Integer.parseInt(args[2]);
    Image iz = Toolkit.getDefaultToolkit().getImage("/home/raspberrypi400/Desktop/4-H CS/Handicraft/Base_images/draw.png");  
    frame.setIconImage(iz);  
    frame.setSize(w,h);
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    frame.setTitle(args[0]);
    frame.setVisible(true);
    Image icon = Toolkit.getDefaultToolkit().getImage(args[3]);  
    frame.setIconImage(icon);
  }
}
