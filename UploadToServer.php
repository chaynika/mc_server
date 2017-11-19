<?php
    $file_path = "/Users/csaikia/Dropbox/Coursework/CSE535/uploaded_files/"; 
    $file_path = $file_path . basename( $_FILES['files']['name']);
    echo $file_path;
    echo $_FILES['files']['tmp_name'];
    if(move_uploaded_file($_FILES['files']['tmp_name'], $file_path)) {
        echo "success";
    } else{
        echo "fail";
    }
 ?>
