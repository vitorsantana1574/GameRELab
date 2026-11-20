package lab.gamere.fabric;

import net.fabricmc.api.ModInitializer;
import net.fabricmc.fabric.api.command.v2.CommandRegistrationCallback;
import net.minecraft.server.command.CommandManager;
import net.minecraft.text.Text;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public final class GameRELabMod implements ModInitializer {
    private static final Logger LOGGER = LoggerFactory.getLogger("gamerelab");

    @Override
    public void onInitialize() {
        LOGGER.info("GameRELab Fabric carregado");
        CommandRegistrationCallback.EVENT.register((dispatcher, registryAccess, environment) ->
            dispatcher.register(CommandManager.literal("gamerelab").executes(context -> {
                context.getSource().sendFeedback(() -> Text.literal("GameRELab pronto."), false);
                return 1;
            }))
        );
    }
}
