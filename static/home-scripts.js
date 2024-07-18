
function openmenu() {
    var menu = document.getElementById('menu');
    menu.style.right = '10px';
}

function closemenu() {
    var menu = document.getElementById('menu');
    menu.style.right = 'calc(-30% - 10px)';
}


function openInOverleaf() {
    // URL of the Overleaf endpoint
    const url = 'https://www.overleaf.com/docs';

    // Parameters to be sent in the POST request
    const params = {
        snip_uri: 'https://venupulagam.s3.ap-south-1.amazonaws.com/cover.tex'
        
    };

    // Create a form element
    const form = document.createElement('form');
    form.method = 'post';
    form.action = url;
    form.target = '_blank';

    // Add parameters as hidden form inputs
    for (const key in params) {
        if (params.hasOwnProperty(key)) {
            const hiddenField = document.createElement('input');
            hiddenField.type = 'hidden';
            hiddenField.name = key;
            hiddenField.value = params[key];
            form.appendChild(hiddenField);
        }
    }

    // Append form to body and submit it
    document.body.appendChild(form);
    form.submit();

    // Remove form from body after submission
    document.body.removeChild(form);
}

function redirectToURL(url) {
    window.open(url, "_blank");
}

function redirect(page) {
    fetch('/redirect', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ page: page })
    })
    .then(response => {
        if (response.redirected) {
            window.location.href = response.url;
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}


function openInOverleaf(username, template) {
    // URL of the Overleaf endpoint
    const url = 'https://www.overleaf.com/docs';

    if (template == 1) {
        params = {
            snip_uri: 'https://' + username + '.s3.ap-south-1.amazonaws.com/' + username + '_classic_single_column.tex'
        };
    } else if (template == 2) {
        params = {
            snip_uri: 'https://' + username + '.s3.ap-south-1.amazonaws.com/' + username + '_classic_double_column.tex'
        };
    } else if (template == 3) {
        params = {
            snip_uri: 'https://' + username + '.s3.ap-south-1.amazonaws.com/' + username + '_professional_single_column.tex'
        };
    }

    // Create a form element
    const form = document.createElement('form');
    form.method = 'post';
    form.action = url;
    form.target = '_blank';

    // Add parameters as hidden form inputs
    for (const key in params) {
        if (params.hasOwnProperty(key)) {
            const hiddenField = document.createElement('input');
            hiddenField.type = 'hidden';
            hiddenField.name = key;
            hiddenField.value = params[key];
            form.appendChild(hiddenField);
        }
    }

    // Append form to body and submit it
    document.body.appendChild(form);
    form.submit();

    // Remove form from body after submission
    document.body.removeChild(form);
}