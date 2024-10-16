package org.example.plugin.service;

import org.example.common.service.CommonService;
import org.example.plugin.config.PluginConfig;

import com.tvd12.ezyfox.bean.annotation.EzyAutoBind;
import com.tvd12.ezyfox.bean.annotation.EzySingleton;

@EzySingleton
public class WelcomeService {

    @EzyAutoBind
    private PluginConfig config;

    @EzyAutoBind
    private CommonService commonService;

    public String welcome(String username) {
        return config.getWelcomePrefix() + " " + username + "!";
    }
}
