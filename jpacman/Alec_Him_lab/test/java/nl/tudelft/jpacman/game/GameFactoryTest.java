package nl.tudelft.jpacman.game;

import static org.assertj.core.api.Assertions.assertThat;
import static org.mockito.Mockito.mock;

import nl.tudelft.jpacman.level.Level;
import nl.tudelft.jpacman.level.PlayerFactory;
import nl.tudelft.jpacman.sprite.PacManSprites;
import nl.tudelft.jpacman.points.PointCalculator;
import nl.tudelft.jpacman.points.PointCalculatorLoader;

import org.junit.jupiter.api.Test;

public class GameFactoryTest {
    /*
     * - GameFactory(PlayerFactory)
     *   > PlayerFactory
     *     - PacManSprites => PlayerFactory
     */
    private final static PacManSprites pms = new PacManSprites();
    private final PlayerFactory factory = new PlayerFactory(pms);
    private final GameFactory gameFac = new GameFactory(factory);

    /*
     * - createSinglePlayerGame(Level, PointCalculator)
     *   > Mock Level
     *   > PointCalculatorLoader => PointCalculator
     */
    private final Level lvl = mock(Level.class);
    private final PointCalculatorLoader pcl = new PointCalculatorLoader();
    private final PointCalculator pc = pcl.load();

    @Test
    void testCreateSinglePlay(){
        assertThat(gameFac.createSinglePlayerGame(lvl, pc)).isNotNull();
    }
}
