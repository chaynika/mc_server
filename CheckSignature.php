<?php
    $file_path = "/Users/csaikia/Dropbox/Coursework/CSE535/uploaded_files/"; 
    $file_path = $file_path . basename( $_FILES['files']['name']);
    if(!move_uploaded_file($_FILES['files']['tmp_name'], $file_path)) {
        echo "fail";
    }
    # TODO comment this line to add the code for comparator
    $mystring = system('python comparator.py 1', $retval);
    #$mystring = system('python comparator.py '.$file_path.' '.$train_file, $retval);
    echo json_encode(array('exit_code' => $retval));
 ?>
