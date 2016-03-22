google.load("visualization", "1", {packages:["table"]});
google.setOnLoadCallback(drawTable);


function drawTable(dataSet,table_div) {

		var cssClassNames = {
								'oddTableRow': 'myAwesomeClass',
							    'tableRow': 'myAwesomeClass',
							 };

		for( i =0; i<dataSet.length; i++)
		{
			dataSet[i][0] = "<b>" + dataSet[i][0] + "</b>";
			dataSet[i][1] = "<b>" + dataSet[i][1] + "</b>";
			
		}					 
        var data = new google.visualization.DataTable();
        data.addColumn('string', '<h3>Twitter Handle</h3>');
        data.addColumn('string', '<h3>Tweet</h3>');
        // data.addColumn('string', '<h3>Text</h3>');
        // data.addColumn('string', 'Link');
        data.addRows(dataSet);

        var view = new google.visualization.DataView(data);
        view.setColumns([0, 1]);

        var table = new google.visualization.Table(document.getElementById(table_div));
		// var table = new google.visualization.Table(document.getElementById('table_div'));

        table_width =  Math.ceil($(window).width()/1.5)
        table_height = Math.ceil($(window).height()/3)
        // table.draw(data, {height: '600px'});
        // table.draw(view, {height: Math.ceil(window.outerHeight/1.5), width: (window.outerWidth/2.2), allowHtml: true});
        table.draw(view, {height: table_height, width: table_width , allowHtml: true,'cssClassNames': cssClassNames});

        function selectHandler(e){
        	
        	console.log(data.getValue(table.getSelection()[0]['row'], 3 ));
          // window.location = data.getValue(table.getSelection()[0]['row'], 3 );
          window.open(data.getValue(table.getSelection()[0]['row'], 3 ));
       }
	google.visualization.events.addListener(table, 'select', selectHandler);
        // console.log("in table");
        // console.log(window.outerHeight/2);
        // showRowNumber: true, page:'enable', pageSize:5,
     };
     
