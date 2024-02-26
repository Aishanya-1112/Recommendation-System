<?php

// Define recipient email address
$to = "aishanya001@gmail.com";

// If form was submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {

  // Sanitize input data to prevent injection attacks
  $name = filter_var($_POST["name"], FILTER_SANITIZE_STRING);
  $email = filter_var($_POST["email"], FILTER_SANITIZE_EMAIL);
  $subject = filter_var($_POST["subject"], FILTER_SANITIZE_STRING);
  $message = filter_var($_POST["message"], FILTER_SANITIZE_STRING);

  // Build the email content
  $body = "Name: " . $name . "\r\n";
  $body .= "Email: " . $email . "\r\n";
  $body .= "Subject: " . $subject . "\r\n";
  $body .= "Message: \r\n" . $message;

  // Set email headers
  $headers = "From: " . $email . "\r\n";
  $headers .= "Content-Type: text/plain; charset=UTF-8\r\n";

  // Send the email
  if (mail($to, $subject, $body, $headers)) {
    echo "sent-message"; // Send success message to JS (replace "echo" with your preferred method)
  } else {
    echo "error-message"; // Send error message to JS (replace "echo" with your preferred method)
  }

} else {
  // Not a POST request, exit
  exit;
}

?>