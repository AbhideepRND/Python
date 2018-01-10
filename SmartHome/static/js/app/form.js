$(document).ready(function(){
             
       var requestObject = {
                     formRegex: {
                                  'name':/^([a-zA-Z0-9])+$/,
                                  'email':/^[\w\-\.\+]+\@[a-zA-Z0-9\.\-]+\.[a-zA-z0-9]{2,4}$/,
                                  'contact':/^([0-9]){10}$/,
                                  'dateformat':/^([0][0-9]{1}|[1][0-9]{1})\/([0,1,2][0-9]{1}|[3][0-1]{1})\/([19,20]{1}[0-9]{2})$/
                     },
                    
                     requestData:null,
                     error:[],
                     init:function(requestData, error){
                           this.requestData = requestData;
                           this.error = error;
                     },
                    
                     getError:function (){
                           return this.error;
                     },
                    
                     getRequestData:function(){
                           return this.requestData;
                     },
                    
                     applyRegex:function(regexName, value){
                           return this.formRegex[regexName].test(value)
                     }
       };

       $("#formSubmit #formBody .form-control").on("change blur keyup",function(e){
        obj = $(this)
        
        try{
            if(isNaN(obj.val())) throw "Not a number";
        } catch(err){
            obj.addClass("is-invalid")
            obj.trigger("focus");
            return false;
        }
            obj.removeClass("is-invalid")
            idVal = obj.attr("id");
            rowNum = idVal.substring(0,4);
            temp=0;
            for(i=1;i<=3;i++){
                    temp=temp+parseInt($("#"+rowNum+i).val())
            }
            $("#"+rowNum+4).val(temp);
            
            if(e.keyCode === 13){

                _colIndex = parseInt(idVal.substring(4,5));
                if(_colIndex === 4 ){
                    _rowIndex = parseInt(idVal.substring(3,4));
                    $('#row'+(_rowIndex+1)+(1)).focus();
                    e.preventDefault();
                } else {
                    $('#'+rowNum+(_colIndex+1)).focus();
                    e.preventDefault();
                }
            }
            return true;
       });

       $("#formSubmit #formBody .form-control").on("focus",function(e){
        $(this).select();
       });

       $("#formSubmit #submit").on("click", function(){
            validateForm(this)
       });

       function validateForm(obj){

            


       }


    });

    