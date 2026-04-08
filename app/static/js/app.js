
async function getUserData(){
    const response = await fetch('/api/users');
    return response.json();
}

function loadTable(users){
    const table = document.querySelector('#result');
    for(let user of users){
        table.innerHTML += `<tr>
            <td>${user.id}</td>
            <td>${user.username}</td>
        </tr>`;
    }
}

async function main(){
    const users = await getUserData();
    loadTable(users);
}

async function loadTotals() {
    const res = await fetch('trackcalories/totals');
    const data = await res.json();

    document.getElementById('calories').innerText = data.calories;
    document.getElementById('protein').innerText = data.protein;
    document.getElementById('carbs').innerText = data.carbs;
    document.getElementById('fat').innerText = data.fat;
}

async function addMeal(id){
    await fetch('/trackcalories/add?meal_id=${id}',{
        method: 'POST'
    });

    loadTotals();
}

main();
