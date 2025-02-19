/** @odoo-module **/
import { registry } from "@web/core/registry";
import { browser } from "@web/core/browser/browser";

function loginAsUser(action) {
    if (!action.params || !action.params.user_id) {
        console.error("User ID is missing in login_as_user action.");
        return;
    }
    const userId = action.params.user_id;
    browser.location = `/web/login?login=${userId}`;
}

registry.category("actions").add("login_as_user", loginAsUser);