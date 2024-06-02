    $(document).ready(function(){
        $("#stuemail").on("keypress blur", function(){
            var stuemail = $("#stuemail").val();
            $.ajax({
                url: "Student/addstudent.php",
                method: "POST",
                data: {
                    checkemail: "checkmail",
                    stuemail: stuemail,
                },
                success: function(data){
                    if(data != 0){
                        $("#statusMsg2").html('<small style="color:red;">El correo ya se encuentra registrado</small>');
                        $("#signup").attr("disabled",true);
                    }else if (data == 0){
                        $("#statusMsg2").html('<small style="color:green;">Correo disponible</small>');
                        $("#signup").attr("disabled",false);
                    }else if(!reg.test(stuemail)){
                        $("#statusMsg2").html('<small style="color:red;">Por favor ingresa una dirección de correo válida p.e. ejemplo@mail.com</small>');
                        $("#signup").attr("disabled",true);
                    }             
                    if(stuemail == ""){
                        $("#statusMsg2").html('<small style="color:red;">Por favor ingresa un correo electrónico</small>');
                    }       
                },
            });
        });
    })    ;
    
    
    
    function addStu(){
        var reg = /^[A-Z0-9._%+-]+@([A-Z0-9-]+\.)+[A-Z]{2,4}$/i;
        var stuname = $("#stuname").val();
        var stuemail = $("#stuemail").val();
        var stupass = $("#stupass").val();

        //Validación de los espacios
        if (stuname.trim() == 0){
            $("#statusMsg1").html('<small style="color:red;">Por favor ingresa un nombre</small>');
            $("#stuname").focus();
            return false; 
        }else if(stuemail.trim() ==""){
            $("#statusMsg2").html('<small style="color:red;">Por favor ingresa un correo electrónico</small>');
            $("#statusMsg1").html('<small style="color:red;"></small>');
            $("#statusMsg3").html('<small style="color:red;"></small>');
            $("#stuemail").focus(); 
        }else if(stuemail.trim() != "" && !reg.test(stuemail)){
            $("#statusMsg2").html('<small style="color:red;">Por favor ingresa una dirección de correo válida p.e. ejemplo@mail.com</small>');
            $("#stuemail").focus(); 
        }else if(stupass.trim() ==""){
            $("#statusMsg3").html('<small style="color:red;">Por favor ingresa una contraseña</small>');
            $("#statusMsg2").html('<small style="color:red;"></small>');
            $("#statusMsg1").html('<small style="color:red;"></small>');
            $("#stupass").focus(); 
            return false; 
        }else{
            $.ajax({
                url:'Student/addstudent.php',
                method: 'POST',
                dataType:"json",
                data:{
                    stusignup: "stusignup",
                    stuname : stuname,
                    stuemail : stuemail,
                    stupass : stupass,
                },
                success:function(data){
                    console.log(data);
                    if(data == "OK"){
                        $('#successMsg').html("<span class='alert alert-success'>Registro exitoso</span>");
                        clearStuRegField();
                    }else if(data == "Failed"){
                        $('#successMsg').html("<span class='alert alert-danger'>No se pudo registrar</span>")
                    }
                }
            })
        }    
    }

    //vaciado de los espacios
    function clearStuRegField(){
        $("#stuRegForm").trigger("reset");
        $("#statusMsg1").html(" ");
        $("#statusMsg2").html(" ");
        $("#statusMsg3").html(" ");
    }


    //Login Ajax
    function checkStuLogin(){
        var stuLogEmail = $("#stuLogemail").val();
        var stuLogPass = $("#stuLogpass").val();
        $.ajax({
            url: "Student/addstudent.php",
            method: "POST",
            data: {
                checkLogemail: "checklogmail",
                stuLogEmail: stuLogEmail,
                stuLogPass: stuLogPass,
            },
            success: function(data){
                if(data == 0){
                    $("#statusLogMsg").html('<small class="alert alert-danger">Correo o contraseña incorrectos</small>');
                }else if (data ==1){
                    $("#statusLogMsg").html('<div class="spinner-border text-success" role="status"></div>');
                    setTimeout(()=>{
                        window.location.href="index.php";
                    }, 1000);
                }
            },
        });
    }