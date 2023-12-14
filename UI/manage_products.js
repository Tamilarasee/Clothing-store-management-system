var productModal = $("#productModal");
    $(function () {

        //JSON data by API call
        //AJAX get reuest->"productListApiUrl" references common_cs.js file and goes to the getproducts function in Server.py file
        //While server is running, this path getproducts keeps displaying the result of function get_products in products_dao file
        //when this AJAX request is successful, the data(response) returned from the server is given to a callback funtion "function(response)"
        
        $.get(productListApiUrl, function (response) {
            if(response) {
                var table = '';
                $.each(response, function(index, product) {
                    table += '<tr>' +
                        '<td>'+ product.product_name +'</td>'+
                        '<td>'+ product.category_name +'</td>'+
                        '<td>'+ product.price_per_unit +'</td>'+
                        '<td><span class="btn btn-xs btn-danger delete-product">Delete</span></td></tr>';
                });
                $("table").find('tbody').empty().html(table);
            }
        });
    });

    // Save Product
    $("#saveProduct").on("click", function () {
        // If we found id value in form then update product detail
        var data = $("#productForm").serializeArray();
        var requestPayload = {
            product_name: null,
            category_id: null,
            price_per_unit: null
        };
        for (var i=0;i<data.length;++i) {
            var element = data[i];
            switch(element.name) {
                case 'name':
                    requestPayload.product_name = element.value;
                    break;
                case 'category':
                    requestPayload.category_id = element.value;
                    break;
                case 'price':
                    requestPayload.price_per_unit = element.value;
                    break;
            }
        }
        callApi("POST", productSaveApiUrl, {
            'data': JSON.stringify(requestPayload)
        });
    });

    $(document).on("click", ".delete-product", function (){
        var tr = $(this).closest('tr');
        var data = {
            product_id : tr.data('id')
        };
        var isDelete = confirm("Are you sure to delete "+ tr.data('name') +" item?");
        if (isDelete) {
            callApi("POST", productDeleteApiUrl, data);
        }
    });

    productModal.on('hide.bs.modal', function(){
        $("#id").val('0');
        $("#name, #category, #price").val('');
        productModal.find('.modal-title').text('Add New Product');
    });

    productModal.on('show.bs.modal', function(){
        //JSON data by API call
        $.get(categoryListApiUrl, function (response) {
            if(response) {
                var options = '<option value="">--Select--</option>';
                $.each(response, function(index, category) {
                    options += '<option value="'+ category.category_id +'">'+ category.category_name +'</option>';
                });
                $("#category").empty().html(options);
            }
        });
    });