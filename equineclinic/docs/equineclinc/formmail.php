<?php
define("FORM_ASSUNTO", "Contato pelo site");
define("FORM_HOSTNAME", "mail.equineclinic.com.br");
define("FORM_USERNAME", "henrique@equineclinic.com.br");
define("FORM_PASSWORD", "Equine2012");
define("FORM_DESTINO",   "henrique@equineclinic.com.br");
define("FROM_REMETENTE_EMAIL", $_REQUEST['email']);
define("FROM_REMETENTE_NOME",  $_REQUEST['nome']);

function retorno() {
	echo "A sua mensagem foi enviada com sucesso !";
	echo "<SCRIPT LANGUAGE=\"javascript\">window.open ('http://www.equineclinic.com.br','_self');</SCRIPT>";
}

function erro($e) {
	printf("Mensagem não foi enviada, erro %s", $e);
}

$conteudo = array(
	'ip' => $_SERVER['REMOTE_ADDR'],
	'data' => date("D M j G:i:s T Y")
);
$conteudo = array_merge($_REQUEST, $conteudo);

/* FORMATACAO HTML */
$msg = '<html><body><table width="100%" border="0">';
foreach ($conteudo as $var => $val) {
	$msg .= sprintf("<tr><td>%s</td> <td>%s</td></tr>\n", $var, $val);
}
$msg .= '</table></body></html>';

require("class.phpmailer.php");

$mail = new PHPMailer();
$mail->IsSMTP();              		     // set mailer to use SMTP
$mail->Host = FORM_HOSTNAME;    	     // specify main and backup server
$mail->SMTPAuth = true;       		     // turn on SMTP authentication
$mail->Username = FORM_USERNAME;             // SMTP username
$mail->Password = FORM_PASSWORD; 	     // SMTP password
$mail->From = FROM_REMETENTE_EMAIL;
$mail->FromName = FROM_REMETENTE_NOME;
$mail->AddAddress(FORM_DESTINO);
$mail->IsHTML(true);                         // set email format to HTML
$mail->Subject = FORM_ASSUNTO;
$mail->Body    = $msg;

if(!$mail->Send()) {
	erro($mail->ErrorInfo);
}

retorno();
?>
