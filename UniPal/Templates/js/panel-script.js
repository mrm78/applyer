        $('[data-toggle="tooltip"]').tooltip();
        var items = document.getElementsByClassName("side-bar-list-item-link");
        items[0].classList.add("side-bar-list-item-link-focus");
        for (let index = 0; index < items.length; index++) {
            items[index].addEventListener("focus", focusIn);
        }

        function focusIn(e) {
            var focusElements = document.getElementsByClassName("side-bar-list-item-link-focus");
            var countElements = document.getElementsByClassName("side-bar-list-item-count-focus");
            for (var index = 0; index < focusElements.length; index++) {
                focusElements[index].classList.remove("side-bar-list-item-link-focus");
            }
            for (var index = 0; index < countElements.length; index++) {
                countElements[index].classList.remove("side-bar-list-item-count-focus");
            }
            e.target.classList.add("side-bar-list-item-link-focus");
            var items = document.getElementsByClassName("side-bar-list-item-link");
            var i = -1;
            for (let index = 0; index < items.length; index++) {
                if (items[index] == e.target) {
                    i = index - 1;
                }
            }
            var countFocusElement = document.getElementsByClassName("side-bar-list-item-count");
            for (var index = 0; index < countFocusElement.length; index++) {
                if (index == i) {
                    countFocusElement[index].classList.add("side-bar-list-item-count-focus");
                }
            }
        }