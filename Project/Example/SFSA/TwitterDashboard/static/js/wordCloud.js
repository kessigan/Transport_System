function cloudPlot(wordlist,canvas_id)
{
    //use this function if the incoming data has a colour in it
    
    // console.log(domain_list);
     // var wordlist = [{"text":"study","size":40},{"text":"motion","size":15},{"text":"forces","size":10},{"text":"electricity","size":15},{"text":"movement","size":10},{"text":"relation","size":5},{"text":"things","size":10},{"text":"force","size":5},{"text":"ad","size":5},{"text":"energy","size":85},{"text":"living","size":5},{"text":"nonliving","size":5},{"text":"laws","size":15},{"text":"speed","size":45},{"text":"velocity","size":30},{"text":"define","size":5},{"text":"constraints","size":5},{"text":"universe","size":10},{"text":"physics","size":120},{"text":"describing","size":5},{"text":"matter","size":90},{"text":"physics-the","size":5},{"text":"world","size":10},{"text":"works","size":10},{"text":"science","size":70},{"text":"interactions","size":30},{"text":"studies","size":5},{"text":"properties","size":45},{"text":"nature","size":40},{"text":"branch","size":30},{"text":"concerned","size":25},{"text":"source","size":40},{"text":"google","size":10},{"text":"defintions","size":5},{"text":"two","size":15},{"text":"grouped","size":15},{"text":"traditional","size":15},{"text":"fields","size":15},{"text":"acoustics","size":15},{"text":"optics","size":15},{"text":"mechanics","size":20},{"text":"thermodynamics","size":15},{"text":"electromagnetism","size":15},{"text":"modern","size":15},{"text":"extensions","size":15},{"text":"thefreedictionary","size":15},{"text":"interaction","size":15},{"text":"org","size":25},{"text":"answers","size":5},{"text":"natural","size":15},{"text":"objects","size":5},{"text":"treats","size":10},{"text":"acting","size":5},{"text":"department","size":5},{"text":"gravitation","size":5},{"text":"heat","size":10},{"text":"light","size":10},{"text":"magnetism","size":10},{"text":"modify","size":5},{"text":"general","size":10},{"text":"bodies","size":5},{"text":"philosophy","size":5},{"text":"brainyquote","size":5},{"text":"words","size":5},{"text":"ph","size":5},{"text":"html","size":5},{"text":"lrl","size":5},{"text":"zgzmeylfwuy","size":5},{"text":"subject","size":5},{"text":"distinguished","size":5},{"text":"chemistry","size":5},{"text":"biology","size":5},{"text":"includes","size":5},{"text":"radiation","size":5},{"text":"sound","size":5},{"text":"structure","size":5},{"text":"atoms","size":5},{"text":"including","size":10},{"text":"atomic","size":10},{"text":"nuclear","size":10},{"text":"cryogenics","size":10},{"text":"solid-state","size":10},{"text":"particle","size":10},{"text":"plasma","size":10},{"text":"deals","size":5},{"text":"merriam-webster","size":5},{"text":"dictionary","size":10},{"text":"analysis","size":5},{"text":"conducted","size":5},{"text":"order","size":5},{"text":"understand","size":5},{"text":"behaves","size":5},{"text":"en","size":5},{"text":"wikipedia","size":5},{"text":"wiki","size":5},{"text":"physics-","size":5},{"text":"physical","size":5},{"text":"behaviour","size":5},{"text":"collinsdictionary","size":5},{"text":"english","size":5},{"text":"time","size":35},{"text":"distance","size":35},{"text":"wheels","size":5},{"text":"revelations","size":5},{"text":"minute","size":5},{"text":"acceleration","size":20},{"text":"torque","size":5},{"text":"wheel","size":5},{"text":"rotations","size":5},{"text":"resistance","size":5},{"text":"momentum","size":5},{"text":"measure","size":10},{"text":"direction","size":10},{"text":"car","size":5},{"text":"add","size":5},{"text":"traveled","size":5},{"text":"weight","size":5},{"text":"electrical","size":5},{"text":"power","size":5}];
    d3.select(canvas_id).select("svg").remove();
    // for( i = 0; i < word_list.length; i++ )
    // {
        // console.log(word_list[i].size);
    // }
    var color = d3.scale.linear()
            .domain([0,1,2,3,4,5,6,10,15,20,100])
            // .range(["#ddd", "#ccc", "#bbb", "#aaa", "#999", "#888", "#777", "#666", "#555", "#444", "#333", "#222"]);
            // .range(["#F06723", "#660099", "#FF6633", "#ff00ff", "#663366", "#009900", "#F02323", "#0033CC", "#ff3366", "#3366ff", "#663300", "#000000", "#484848", "#ff6600", "#99ff00" ]);
            .range(
                [   "#660066", "#FF0066", "#006699", "#0066CC", "#00FFCC", "#6633CC", "#9966CC",
                    "#FF00CC", "#787878 ", "#ff7d69", "#778899", "#CD853F", "#BA55D3", "#000080",
                    "#FF6347", "#87CEEB", "#FFA500", "#FF4500", "#FF0000", "#008080", "#00FFFF", 
                    "#011d01", "#003300", "#330000", "#333300", "#660000", "#663300", "#993300", 
                    "#000033", "#003333", "#330033", "#333333", "#CC0033", "#003366", "#333366"  
                ] 
            );

    // d3.layout.cloud().size([800, 300])
    // d3.layout.cloud().size([$(window).width()/4, $(window).height()/5])
    d3.layout.cloud().size([Math.ceil($(window).width()/2), Math.ceil($(window).height()/4.5)])
            .words(wordlist)
            .rotate(0)
            .fontSize(function(d) { return d.size; })
            .on("end", draw)
            .start();

    function draw(words) {
        // var w = Math.ceil($(window).width()/3/3);
        // var h = Math.ceil($(window).height()/2.5/2.05);
        var my_height = Math.ceil($(window).height()/1.5);

        // var w = Math.ceil($(window).width()/3/2.3);
        // var h = Math.ceil($(window).height()/2);
        
        var w = Math.ceil($(window).width()/3/3);
        var h = Math.ceil($(window).height()/2.5/2.05);

        d3.select(canvas_id).append("svg")
                // .attr("width", 525)
                // .attr("height", 390)
                // .attr("width", $(window).width()/3)
                // .attr("height", $(window).height()/2.5)
                // .attr("width", $(window).width()/3)
                // .attr("height", Math.ceil($(window).height()/3))
                .attr("width", $(window).width()/1.7)
                .attr("height", Math.ceil($(window).height()/2.5))
                .attr("class", "wordcloud")
                .append("g")
                // without the transform, words words would get cutoff to the left and top, they would
                // appear outside of the SVG area
                // .attr("transform", "translate(220,190)")
                .attr("transform", "translate(" + w*1.5 + "," + h + ")")
                .selectAll("text")
                .data(words)
                .enter().append("text")
                .style("font-size", function(d) { return d.size + "px"; })
                .style("fill", function(d, i) {                                                 
                                                    return d["colour"];
                                                    // return color(i); 
                                                })
                .attr("transform", function(d) {
                    return "translate(" + [d.x, d.y] + ")rotate(" + d.rotate + ")";
                })
                .on("click", function (d, i){
                                            
                                                // d3.select("#display_text").attr("style","background-color:#D8D8D8; font-size:4;").text(d.text_appearance).style("color", "black");
                                                table_id = "table_div";
                                                

                                                dataSet1 = d.text_appearance;

                                                //THIS IS A google visualisation table
                                                drawTableWordThree(dataSet1,table_id,my_height);
                                                
                                                window.onresize = function() {
                
                                        drawTableWordThree(dataSet1,table_id,my_height);
                                        
                                };
                                                //THIS IS A datatables table
                                                // drawDtTableAgric(dataSet1);


                                                 // window.open(d.url, "_blank");

                                            })
                .text(function(d) { return d.text; });

    }
};