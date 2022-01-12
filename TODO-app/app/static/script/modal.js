$(document).ready(function () {
    
    if (localStorage.getItem("theme") === "dark") {
        $("body").css("background-color", "hsl(200, 65%, 8%)");
        $("body").css("color", "white");
        $(".table").css("color", "white");
        $(".toggle").attr("checked", false);
        $(".footer").css("background-color", "hsl(200, 65%, 8%)");
        $(".text-muted").css("color", "white");
      
    }
    else{ 
        $("body").css("background-color", "white");
        $("body").css("color", "black");
        $(".table").css("color", "black");
        $(".toggle").attr("checked", true);
        $(".footer").css("background-color", "white");
        $(".text-muted").css("color", "black");
    
    }


    $('.toggle').click(function () {
        if ($(this).is(':checked')) {
            $("body").css("background-color", "white");
            $("body").css("color", "black");
            $(".table").css("color", "black");
            $(".footer").css("background-color", "white");
            $(".text-muted").css("color", "black");
            localStorage.setItem("theme", "light");
        }
        else{ 
            $("body").css("background-color", "hsl(200, 65%, 8%)");
            $("body").css("color", "white");
            $(".table").css("color", "white");
            localStorage.setItem("theme", "dark");
            $(".footer").css("background-color", "hsl(200, 65%, 8%)");
            $(".text-muted").css("color", "white");
            
           
        }
    });

    $('#task-modal').on('show.bs.modal', function (event) {
        const button = $(event.relatedTarget) // Button that triggered the modal
        const taskID = button.data('source') // Extract info from data-* attributes
        const content = button.data('content') // Extract info from data-* attributes
        const date = button.data('date') // Extract info from data-* attributes
        const hour = button.data('hour') // Extract info from data-* attributes
        

        const modal = $(this)
        if (taskID === 'New Task') {
            modal.find('.modal-title').text(taskID)
            $('#task-form-display').removeAttr('taskID')
        } else {
            modal.find('.modal-title').text('Edit Task ' + taskID)
            $('#task-form-display').attr('taskID', taskID)
        }

        if (content) {
            modal.find('#task-form').val(content);
            modal.find('#date-form').val(date);
            modal.find('#hour-form').val(hour);

        } else {
            modal.find('.form-control').val('');
        }
    })


    $('#submit-task').click(function () {
        const tID = $('#task-form-display').attr('taskID');
        console.log($('#task-modal').find('#task-form').val())
        console.log($('#task-modal').find('#date-form').val())
        console.log($('#task-modal').find('#hour-form').val())
        $.ajax({
            type: 'POST',
            url: tID ? '/edit/' + tID : '/create',
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({
                'description': $('#task-modal').find('#task-form').val(),
                'date': $('#task-modal').find('#date-form').val(),
                'hour': $('#task-modal').find('#hour-form').val()
            }),
            success: function (res) {
                console.log(res.response)
                location.reload();
            },
            error: function () {
                console.log('Error');
            }
        });
    });

    $('.remove').click(function () {
        const remove = $(this)
        $.ajax({
            type: 'POST',
            url: '/delete/' + remove.data('source'),
            success: function (res) {
                console.log(res.response)
                location.reload();
            },
            error: function () {
                console.log('Error');
            }
        });
    });

    $('.state').click(function () {
        const state = $(this)
        const tID = state.data('source')
        
        if (state.text() === "In Progress") {
            new_state = "Complete"
        } else if (state.text() === "Complete") {
            new_state = "Todo"
        } else if (state.text() === "Todo") {
            new_state = "In Progress"
        }

        $.ajax({
            type: 'POST',
            url: '/edit/' + tID,
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({
                'status': new_state
            }),
            success: function (res) {
                console.log(res)
                location.reload();
            },
            error: function () {
                console.log('Error');
            }
        });
    });

});