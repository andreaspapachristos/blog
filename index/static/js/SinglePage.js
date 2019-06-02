spa.shell = function () {
    var
        configMap = {
            main_html: String()
                + '<div class="spashell-head">'
                + '<div class="spashell-head_logo"></div>'
                + '<div class="spashell-head_acct"></div>'
                + '<div class=""spashell-head_search"></div>'
                + '</div>'
                + '<div class="spashell-main"> '
                + '<div class="spashell-main_nav"></div>'
                + '<div class="spashell-main_content>"></div>'
                + '</div>'
                + '<div class="spashell-foot"></div>'
                + '<div class="spashell-modal"></div>',
            chat_extend_time: 1000,
            chat_retract_time: 300,
            chat_extend_height: 450,
            chat_retrack_height: 15,
            chat_extended_title: 'Click to retract',
            chat_retracked_title: 'Click to extend'
        },
        stateMap = {
            $container: null,
            is_chat_retracted: true
        },
        jqueryMap = {},
        initModule;
    jqueryMap = {
        $container: $container,
        $chat: $container.find('.spa-shell-chat')
    };
    toggleChat = function (do_extend, callback) {
        var
            px_chat_ht = jqueryMap.$chat.height(),
            is_open = px_chat_ht === configMap.chat_extended_height,
            is_closed = px_chat_ht === configMap.chat_retrack_height,
            is_sliding = !is_open && !is_closed;
        if (is_sliding) {
            return false;
        }
        if (do_extend) {
            jqueryMap.$chat.animate(
                {height: configMap.chat_extended_height}
            configMap.chat_extended_time,
                function () {
                    jqueryMap.$chat.attr(
                        'title', configMap.chat_extended_title
                    );
                    stateMap.is_chat_retracted = false;
                    if (callback) {
                        callback(jqueryMap.$chat);
                    }
                }
        )
            ;
            return true;
        }
        jqueryMap.$chat.animate(
            {height: configMap.chat_retrack_height},
            configMap.chat_retract_time,
            function () {
                jqueryMap.$chat.attr(
                    'title', configMap.chat_retracked_title
                );
                stateMap.is_chat_retracted = true;
                if (callback) {
                    callback(jqueryMap.$chat);
                }
            }
        );
        return true;

        onclickChat = function (event) {
            toggleChat(stateMap.is_chat_retracted);
            return false;
        };

    }();
    setJqueryMap = function () {
        var $container = stateMap.container;
        jqueryMap = {$container: $container};
    };

    initModule = function ($container) {
        stateMap.$container = $container;
        $container.html(configMap.main_html);
        setJqueryMap.$chat
            .attr('title', configMap.chat_retracked_title)
            .click(onclickChat);
    };
    return {initModule: initModule};

}();