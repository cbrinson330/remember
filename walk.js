//recursive function to access each child node of a dom element used with undraw
function walk(children) {
  if (typeof children == "undefined" || children.size() === 0) {
    return;
  } 
  children.each(function(){
    var child = $(this);
    if (child.children().size() > 0) {
      walk(child.children());
    } 
    cleanNode(child);
  });
} 
