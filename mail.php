<?php

// $recepient = "ali.boulhajat@gmail.com";
// $sitename = "Boulhajat Portfolio";

// $name = trim($_POST["name"]);
// $email = trim($_POST["email"]);
// $text = trim($_POST["text"]);
// $message = "Name: $name \nEmail: $email \nText: $text";

// $pagetitle = "New message from the \"$sitename\"";
// mail($recepient, $pagetitle, $message, "Content-type: text/plain; charset=\"utf-8\"\n From: $recepient");

if(isset($_POST['submit'])){
    $to = "ali.boulhajat@gmail.com"; // this is your Email address
    $from = $_POST['email']; // this is the sender's Email address
    $name = $_POST['name'];
    $message = "Name: $name \nEmail: $email \nText: $text";

    $result =  @mail($to,$subject,$message);
    // echo "Mail Sent. Thank you " . $first_name . ", we will contact you shortly.";
    // You can also use header('Location: thank_you.php'); to redirect to another page.
    // You cannot use header and echo together. It's one or the other.
    }

?>