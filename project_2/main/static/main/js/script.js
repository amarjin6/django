var count = 1;
function add()
{
    var input = document.createElement("INPUT");
    input.name = 'name' + count;
    input.type = "text";
    input.id = "name" + count;
    input.className = "form-control input";
    document.getElementById('form-group').appendChild(input);
    count++;
}