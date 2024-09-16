import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.io.*;
import java.net.*;

public class LoginUI extends JFrame implements ActionListener {
    private JTextField usernameField;
    private JPasswordField passwordField;
    private JButton signupButton;
    private JButton loginButton;
    private JLabel messageLabel;

    private Socket socket;

    public LoginUI() {
        // Set up the JFrame
        setTitle("Login System");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setSize(300, 200);
        setLayout(new GridLayout(5, 1));

        // Create UI elements
        usernameField = new JTextField();
        passwordField = new JPasswordField();
        signupButton = new JButton("Sign Up");
        loginButton = new JButton("Log In");
        messageLabel = new JLabel(" ");

        // Add action listeners
        signupButton.addActionListener(this);
        loginButton.addActionListener(this);

        // Add elements to the frame
        add(new JLabel("Username:"));
        add(usernameField);
        add(new JLabel("Password:"));
        add(passwordField);
        add(signupButton);
        add(loginButton);
        add(messageLabel);

        // Make the frame visible
        setVisible(true);
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        if (e.getSource() == signupButton) {
            handleSignup();
        } else if (e.getSource() == loginButton) {
            handleLogin();
        }
    }

    private void handleSignup() {
        String username = usernameField.getText();
        String password = new String(passwordField.getPassword());

        try {
            socket = new Socket("127.0.0.1", 65432); // Connect to the Python server
            PrintWriter out = new PrintWriter(socket.getOutputStream(), true);
            BufferedReader in = new BufferedReader