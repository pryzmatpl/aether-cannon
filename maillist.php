<?php

header('Content-Type: application/json');

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405);
    echo json_encode(['error' => 'Method not allowed']);
    exit;
}

$input = json_decode(file_get_contents('php://input'), true);

if (!isset($input['email']) || !filter_var($input['email'], FILTER_VALIDATE_EMAIL)) {
    http_response_code(400);
    echo json_encode(['error' => 'Invalid email address']);
    exit;
}

$sku = isset($input['sku']) ? htmlspecialchars($input['sku']) : 'unknown';
$to = isset($input['to']) ? filter_var($input['to'], FILTER_VALIDATE_EMAIL) : 'pryzmat@pryzmat.pl';
$email = $input['email'];

$subject = "New Waitlist Signup: $sku";
$message = "A new user has signed up for the waitlist.\n\nEmail: $email\nSKU: $sku";
$headers = "From: noreply@pryzmat.pl\r\nReply-To: noreply@pryzmat.pl\r\nContent-Type: text/plain; charset=UTF-8";

if (mail($to, $subject, $message, $headers)) {
    mail("piotr.slupski@pryzmat.pl", $subject, $message, $headers);
    echo json_encode(['success' => 'Successfully joined the waitlist']);
} else {
    http_response_code(500);
    echo json_encode(['error' => 'Failed to send email']);
}
