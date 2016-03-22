function createHeatMap(){
 // add all your code to this method, as this will ensure that page is loaded
  var surr_div = document.getElementById("map_container");
  console.log(surr_div);
  var temp_height = surr_div.offsetHeight;   
  console.log(temp_height);  
  var provincedata = [ {
      id: "LS",
      value: 4447100
    }, {
      id: "ZA-EC",
      value: 626932
    }, {
      id: "ZA-FS",
      value: 5130632
    }, {
      id: "ZA-GT",
      value: 2673400
    }, {
      id: "ZA-LP",
      value: 33871648
    }, {
      id: "ZA-MP",
      value: 4301261
    }, {
      id: "ZA-NC",
      value: 3405565
    }, {
      id: "ZA-NL",
      value: 783600
    }, {
      id: "ZA-MP",
      value: 15982378
    }, {
      id: "ZA-NC",
      value: 8186453
    }, {
      id: "ZA-NL",
      value: 1211537
    }, {
      id: "ZA-NW",
      value: 1293953
    }, {
      id: "ZA-WC",
      value: 12419293
    } ]; 
           
		    var map = AmCharts.makeChart( "hellomap", {
				  type: "map",
				  "theme": "light",

				  colorSteps: 10,
				
				  dataProvider: {
				    map: "southAfricaLow",
		            areas: provincedata 
				  },
				
				  areasSettings: {
				   autoZoom: true,
				   rollOverColor: "#009ce0"
				 },
				
				  valueLegend: {
				    right: temp_height,
				    minValue: "low",
				    maxValue: "high"
				  },
				
				  "export": {
				    "enabled": true
				  }
		
			} );
			
			map.categoryField = "id";
			
			map.areasSettings = { 
  				rollOverColor: "#009ce0", 
  				selectable: true
			};
			
		    map.addListener("clickMapObject",handleClick);// function(event) {alert("This message should appear when I click on a province.");
					 
   }
    
    function handleClick(event)
	{
    	//alert(event.mapObject.id + ": " + event.mapObject.title);

    	var temp = event.mapObject.id + "";
    	
    	//re-map to database province codes 
    	if 	(temp.substring(3, 5) == "GT"){
    		serviceByProvince.filter("GP");
    	}
    	else if(temp.substring(3, 5) == "NL"){
    		serviceByProvince.filter("KZ");
    	}
    	else if(temp.substring(3, 5) == "EC"){
    		serviceByProvince.filter("ES");
    	}
    	else{
    		serviceByProvince.filter(temp.substring(3, 5));
    	}
    	renderAll();
    	
	}
    
    
    function mapProvinceAMPMap(str){
    	if (str =="GP"){return "ZA-GT";}
    	else if (str == "FS"){ return "ZA-FS";}
    	else if (str == "ES"){ return "ZA-EC";}
    	else if (str == "EC"){ return "ZA-EC";}
    	else if (str == "NW"){ return "ZA-NW";}
    	else if (str == "MP"){ return "ZA-MP";}
    	else if (str == "KZ"){ return "ZA-NL";}
    	else if (str == "WC"){ return "ZA-WC";}
    	else if (str == "NC"){ return "ZA-NC";}
    	else if (str == "LP"){ return "ZA-LP";}
    	else return "NULL";
 	
    }