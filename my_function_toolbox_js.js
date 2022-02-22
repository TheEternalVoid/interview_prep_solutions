function findLowestStartingStair(jumps) {
	let i;
	let startingStair = 0
	let currentStair;
	let done = false;

	while (!done){
  		startingStair++;
  		currentStair = startingStair;
  		done = true;
  	for(i = 0; i != jumps.length; i++){
    	currentStair += jumps[i];
    	if (currentStair < 1) {
      		done = false;
     		break;
   		}
  	}
}
return startingStair;	
}