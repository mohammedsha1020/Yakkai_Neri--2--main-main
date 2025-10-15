// Script to update HTML templates from Flask/Jinja2 to Express-compatible format
const fs = require('fs');
const path = require('path');

const templatesDir = path.join(__dirname, '../templates');

function convertTemplate(content) {
  // Replace {{ url_for('static', filename='...') }} with /static/...
  content = content.replace(
    /\{\{\s*url_for\('static',\s*filename='([^']+)'\)\s*\}\}/g,
    '/static/$1'
  );
  
  // Replace {{ url_for('route_name') }} with /route-name
  const routeMap = {
    'home': '/',
    'wellness_form': '/wellness_form',
    'corporate_onboard': '/corporate_onboard',
    'corporate_yoga': '/corporate-yoga',
    'submit_corporate_wellness': '/submit_corporate_wellness',
    'submit_wellness': '/submit_wellness',
    'submit_company': '/submit_company',
    'courses': '/courses',
    'contact': '/contact',
    'meet_the_trainer': '/meet-the-trainer',
    'workshops': '/workshops'
  };
  
  Object.entries(routeMap).forEach(([flaskRoute, expressRoute]) => {
    const regex = new RegExp(`\\{\\{\\s*url_for\\('${flaskRoute}'\\)\\s*\\}\\}`, 'g');
    content = content.replace(regex, expressRoute);
  });
  
  // Replace any remaining {{ company_code }} or similar variables with EJS syntax
  content = content.replace(/\{\{\s*(\w+)\s*\}\}/g, '<%= $1 %>');
  
  return content;
}

function processTemplates() {
  const files = fs.readdirSync(templatesDir);
  
  files.forEach(file => {
    if (file.endsWith('.html')) {
      const filePath = path.join(templatesDir, file);
      let content = fs.readFileSync(filePath, 'utf8');
      
      const originalContent = content;
      content = convertTemplate(content);
      
      if (content !== originalContent) {
        // Rename to .ejs
        const newFilePath = filePath.replace('.html', '.ejs');
        fs.writeFileSync(newFilePath, content, 'utf8');
        console.log(`✅ Converted: ${file} -> ${file.replace('.html', '.ejs')}`);
      }
    }
  });
  
  console.log('\n✅ Template conversion complete!');
}

if (require.main === module) {
  processTemplates();
}

module.exports = { convertTemplate, processTemplates };
